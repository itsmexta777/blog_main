from django import forms

from .models import Comment

class commentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email','body']