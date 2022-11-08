from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

# class ContactForm(forms.Forms):
#     name=forms.CharField(max_length=50, label='Name')
#     surname=forms.CharField(max_length=50, label='Surname')
#     email=forms.EmailField(max_length=50, label='Email')
    