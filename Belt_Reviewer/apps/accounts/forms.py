# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist.')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect pasword.')
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(label='Alias', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email address', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'name',
            'username',
            'email',
            'password',
            'confirm_password',
        ]

    def clean(self, *args, **kwargs):
        # print(self.cleaned_data)
        email = self.cleaned_data.get('email')
        registration_email = User.objects.filter(email=email)
        if registration_email.exists():
            raise forms.ValidationError('This email already exists.')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match.')
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Alias', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['name', ]
