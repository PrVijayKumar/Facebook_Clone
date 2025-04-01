from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework import serializers

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    #  Configuration
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserCreationForm(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    email = serializers.EmailField(required=True)
    is_staff = serializers.BooleanField(required=False, default=False)
