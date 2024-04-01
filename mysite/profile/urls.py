from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='registration'),
    path('login/', views.login_user, name='login'),
    path('update/', views.update_user, name='update'),
]