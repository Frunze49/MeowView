from django import forms


class PostForm(forms.Form):
    description = forms.CharField(max_length=100)
    image = forms.ImageField()