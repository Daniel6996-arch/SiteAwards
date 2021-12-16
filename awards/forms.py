from django import forms
from .models import Website

class SiteForm(forms.ModelForm):
    image = forms.FileField(label='Upload Landing page image') 

    class Meta:
        model = Website
        exclude = ['author', 'uploaded_on']