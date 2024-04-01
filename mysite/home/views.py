from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@api_view(['GET'])
def home_page(request):
    return render(request, 'index.html')
