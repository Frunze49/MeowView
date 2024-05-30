from django.shortcuts import redirect, render

def show_docs(request):
    return render(request, 'openapi.html')