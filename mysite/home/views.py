from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

import grpc
import grpc_api.posts_pb2 as posts_pb2
import grpc_api.posts_pb2_grpc as posts_pb2_grpc

from PIL import Image
from io import BytesIO
import sys
import base64
import os

from .forms import PostForm

grpc_host = 'postgresql' # temp
grpc_port = '50051'

@csrf_exempt
@login_required
@api_view(['GET'])
def home_page(request):
    page = 1
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    return render(request, 'index.html', {'posts': show_posts(request, page), 'current_page': page})

@csrf_exempt
@login_required
def show_posts(request, page_number):
    with grpc.insecure_channel(f"{grpc_host}:{grpc_port}") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.ListPost(posts_pb2.ListRequest())

    tmp = []

    paginator = Paginator(response.list, 1)
    page_obj = paginator.get_page(page_number)

    for i in page_obj:
        tmp.append(
            {
                'id': i.id,
                'login': i.login,
                'description': i.description,
                'image': base64.b64encode(i.image).decode('utf-8')
            }
        )

    return {'page': tmp, 'num_pages': paginator.num_pages}

@csrf_exempt
@login_required
def get_post(request, id):
    with grpc.insecure_channel(f"{grpc_host}:{grpc_port}") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.GetPost(posts_pb2.GetRequest(id=id, login=request.user.username))

    tmp =   {
                'id': response.post.id,
                'login': response.post.login,
                'description': response.post.description,
                'image': base64.b64encode(response.post.image).decode('utf-8')
            }

    return render(request, 'get_post.html', {'post': tmp, 'permission': response.post.login == request.user.username})


@csrf_exempt
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        response = None
        if post_form.is_valid():
            image_file = post_form.cleaned_data['image']

            with grpc.insecure_channel(f"{grpc_host}:{grpc_port}") as channel:
                stub = posts_pb2_grpc.GreeterStub(channel)
                post = posts_pb2.Post(
                    login=request.user.username,
                    description=post_form.cleaned_data['description'],
                    image=image_file.read()
                )
                response = stub.AddPost(posts_pb2.AddRequest(post=post))

        if response and response.success:
            messages.success(request, _('Your post was successfully created!'))
            return redirect('home_page')
        
        messages.error(request, _('Something went wrong.'))
        context = {}
        context['form'] = post_form
        return render(request, 'add_post.html', context)
    
    context = {}
    context['form'] = PostForm()
    return render(request, 'add_post.html', context)

@csrf_exempt
@login_required
def delete_post(request, id):
    with grpc.insecure_channel(f"{grpc_host}:{grpc_port}") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.DeletePost(posts_pb2.DeleteRequest(id=id, login=request.user.username))
    if response.success:
        return redirect('home_page')
    
    return get_post(request=request, id=id)


@csrf_exempt
@login_required
def update_post(request, id):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        response = None
        if post_form.is_valid():
            image_file = post_form.cleaned_data['image']

            with grpc.insecure_channel(f"{grpc_host}:{grpc_port}") as channel:
                stub = posts_pb2_grpc.GreeterStub(channel)
                post = posts_pb2.Post(
                    id=id,
                    login=request.user.username,
                    description=post_form.cleaned_data['description'],
                    image=image_file.read()
                )
                response = stub.UpdatePost(posts_pb2.UpdateRequest(post=post))

        if response and response.success:
            messages.success(request, _('Your post was successfully created!'))
            return redirect('home_page')
        
        messages.error(request, _('Something went wrong.'))
        context = {}
        context['form'] = post_form
        return render(request, 'add_post.html', context)
    
    context = {}
    context['form'] = PostForm()
    return render(request, 'add_post.html', context)


