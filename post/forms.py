from django import forms
from django.forms import TextInput, EmailInput

from .models import Comment, Contact

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your comment...'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
