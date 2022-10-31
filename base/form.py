from django import forms
from .models import TodoApp

class TodoAppForm(forms.ModelForm):

    class Meta:
        model = TodoApp
        fields = '__all__'


