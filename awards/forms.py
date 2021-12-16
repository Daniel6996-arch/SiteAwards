from django import forms
from .models import Website

class SiteForm(forms.ModelForm):
    #image = forms.FileField(label='Upload Landing page image') 

    class Meta:
        model = Website
        exclude = ['author', 'uploaded_on']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label = '',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder':'Comment Something...'
        })   
    )

    class Meta:
        model = Comment
        fields = ['comment']        