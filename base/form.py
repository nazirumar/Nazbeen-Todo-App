from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from .models import TodoApp

class TodoAppForm(forms.ModelForm):

    class Meta:
        model = TodoApp
        fields = '__all__'
        widgets = {
        'created': forms.DateInput(attrs={'type': 'date'}),
    }
