from email.mime import image
from django import forms
from django.core.exceptions import ValidationError
from post.models import Post, Comment


class Form_post(forms.Form):
    title = forms.CharField(max_length=300)
    subtitle = forms.CharField(max_length=500)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    date = forms.DateField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'image',]

class Form_comment(forms.Form):
    post = forms.CharField()
    author = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    body = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Comment
        fields = ['body']


class Search_post(forms.Form):
    title = forms.CharField(max_length=50)