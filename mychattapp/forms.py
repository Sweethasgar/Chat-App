from django import forms
from django.forms import ModelForm
from .models import Chattmessage

class ChatMessageForm(ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder":"type here"}))
    class Meta: 
        model=Chattmessage
        fields = ["body",]

