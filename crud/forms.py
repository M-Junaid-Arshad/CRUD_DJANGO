from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Information

class InfoModelForm(forms.ModelForm):
    class  Meta:
        model = Information
        fields = '__all__'