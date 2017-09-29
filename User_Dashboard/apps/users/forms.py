# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *


User = get_user_model()


class UserLoginForm(forms.Form):
    """
    User login form
    """
    username = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist.')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect pasword.')
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')

        return super(UserLoginForm, self).clean(*args, **kwargs)
    # email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # # username = forms.CharField(label='Email address', widget=forms.EmailInput(
    # #     attrs={'class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     # username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     # if username and password:
    #     if email and password:
    #         username = User.objects.get(email=email).username
    #         authenticate_user = authenticate(username=username, password=password)
    #         find_user = User.objects.filter(username=username)
    #         if not find_user.exists():
    #             raise forms.ValidationError('This user does not exist.')
    #         if not authenticate_user:
    #             raise forms.ValidationError('Your email or password was not entered correctly.')
    #         # if not user.is_active:
    #         #     raise forms.ValidationError('This user is no longer active.')
    #     return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    """
    User registration form
    """
    birthday = forms.DateField(required=False, widget=forms.DateInput(
        format="%m/%d/%Y", attrs={'class': 'form-control', 'type': 'date'}))
    password = forms.CharField(required=True, label='Create Password', widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))
    # name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    # username = forms.CharField(
    #     label='Alias', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label='Email address', required=True, widget=forms.EmailInput(
    #     attrs={'class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))
    # confirm_password = forms.CharField(
    #     widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'birthday',
            'password',
            'confirm_password',
        ]
        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'username': 'Site Username',
            'email': 'Your Email Address',
            # 'birthday': 'Your Birthdate',
            # 'password': 'Create Password',
            # 'confirm_password': 'Confirm Password',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'birthday': forms.DateInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}),
        #     'confirm_password': forms.PasswordInput(render_value=False, attrs={'class': 'form-control'}),
        }

    def clean(self, *args, **kwargs):
        # Validate password confirmation
        print(self.cleaned_data)
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Your passwords must match.')
        # Check if user exists
        email = self.cleaned_data.get('email')
        registration_email = User.objects.filter(email=email)
        if registration_email.exists():
            raise forms.ValidationError('This email is already registered to an account.')
        return super(UserRegistrationForm, self).clean(*args, **kwargs)


class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y", attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
            model = UserProfile
            fields = ['birthday', ]
