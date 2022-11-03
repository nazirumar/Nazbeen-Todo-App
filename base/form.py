from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import TodoApp

class TodoAppForm(forms.ModelForm):

    class Meta:
        model = TodoApp
        fields = '__all__'
        exclude =('user', 'slug',)
        widgets = {
        'created': forms.DateInput(attrs={'type': 'date'}),
    }

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        description = data.get('description')
        return data


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean(self):
    #     data = self.cleaned_data
    #     username = data.get('username')
    #     email = data.get('email')
    #     password1 = data.get('password1')
    #     password2 = data.get('password2')
    #     return super().clean() 