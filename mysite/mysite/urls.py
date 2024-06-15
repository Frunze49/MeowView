from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", include("home.urls")),
    path("user/", include("profile.urls")),
    path("admin/", admin.site.urls),
    path('docs/', views.show_docs, name='docs'),
]