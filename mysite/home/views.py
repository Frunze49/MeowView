from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.contrib import messages

import grpc
import grpc_api.posts_pb2 as posts_pb2
import grpc_api.posts_pb2_grpc as posts_pb2_grpc

from .forms import PostForm


@login_required
@api_view(['GET'])
def home_page(request):
    return render(request, 'index.html', {'posts': show_posts()})


def show_posts():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.ListPost(posts_pb2.ListRequest())

    return response.list

def get_post(request, id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.GetPost(posts_pb2.GetRequest(id=id, login=request.user.username))

    return response.post


@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        response = None
        print(post_form.data['description'])
        print(post_form.is_valid())
        if post_form.is_valid():
            image_file = post_form.cleaned_data['image']

            with grpc.insecure_channel("localhost:50051") as channel:
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
    else:
        context = {}
        context['form'] = PostForm()
        return render(request, 'add_post.html', context)


@login_required
def delete_post(request, id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.DeletePost(posts_pb2.DeleteRequest(id=id, login=request.user.username))
    return response.success


@login_required
def update_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        response = None
        if post_form.is_valid():
            image_file = post_form.cleaned_data['image']

            with grpc.insecure_channel("localhost:50051") as channel:
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
    else:
        post = get_post(request, id)
        context = {}
        context['form'] = PostForm()
        return render(request, 'update_post.html', context)

