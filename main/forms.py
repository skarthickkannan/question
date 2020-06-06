from .models import Post, Answer, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'comments']


class UserForm(UserCreationForm):
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']