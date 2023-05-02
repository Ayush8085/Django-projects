from django import forms
from django.forms import ModelForm
from .models import Tasks

class TasksForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your task here'}))

    class Meta:
        model = Tasks
        fields = '__all__'