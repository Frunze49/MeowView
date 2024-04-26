from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('home/add_post', views.add_post, name='add_post'),
    path('home/<int:id>/', views.get_post, name='get_post'),
    path('home/<int:id>/', views.delete_post, name='delete_post'),
    path('home/<int:id>/', views.update_post, name='update_post'),
]