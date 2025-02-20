from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['title', 'url', 'description']
