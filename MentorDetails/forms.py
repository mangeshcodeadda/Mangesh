from dataclasses import field
from django import forms
from .models import mentord

class Mentord(forms.ModelForm):
    class Meta:
        model=mentord
        fields='__all__'