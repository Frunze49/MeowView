from .models import Profile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'phone_number')

class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')