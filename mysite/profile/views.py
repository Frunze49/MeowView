from datetime import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import User
from .forms import UserForm, ProfileForm, RegForm


@csrf_exempt # for tests
def register_user(request):

    context = {}
    status_code = 200

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if username in [None, ''] or password in [None, '']:
            status_code = 400
            return render(request, 'register.html', context=context, status=status_code)

        try:
            user = User.objects.get(username=username)
            messages.error(request, _('Username already in use :('))
            status_code = 400

        except User.DoesNotExist:
            user = User.objects.create(username=username)
            user.set_password(password)  # Здесь пароль будет автоматически хэширован
            user.save()

            return redirect('login')
        
    return render(request, 'register.html', context=context, status=status_code)
    

@csrf_exempt # for tests
def login_user(request):
    status = 200
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, _('Incorrect username or password :('))
            status = 401  
    return render(request, 'login.html', status=status)
            


@login_required(login_url='/user/login/')
@transaction.atomic
@csrf_exempt # for tests
def update_user(request):
    context = {}
    status_code = 200
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home_page')
        else:
            messages.error(request, _('Incorrect form :('))
            status_code = 400
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        user_date = profile_form['birthday'].value()
        phone_number = profile_form['phone_number'].value()
        if phone_number is None:
            phone_number = ''

        user_date_str = ''
        if user_date:
            user_date_str = user_date.strftime("%Y-%m-%d")

        context = {
            'user_form': user_form,
            'phone_number': phone_number,
            'user_birthday': user_date_str
        }

    return render(request, 'update.html', context=context, status=status_code)


def show_docs(request):
    return render(request, 'openapi.html')

