from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from .models import User
from .forms import UserForm, ProfileForm, RegForm


def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            messages.error(request, _('Username already in use :('))

        except User.DoesNotExist:
            user = User.objects.create(username=username)
            user.set_password(password)  # Здесь пароль будет автоматически хэширован
            user.save()

            messages.success(request, _('Your profile was successfully created!'))
            return redirect('login')
    return render(request, 'register.html')
    

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        err = {'error': 'Invalid username or password'}
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('update')
            
    return render(request, 'login.html')
            

@login_required(login_url='/user/login/')
@transaction.atomic
def update_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home_page')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update.html')
