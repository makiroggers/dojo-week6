# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import HttpResponse, redirect, render
from .forms import *


def index(request):
    """
    Renders registration and login forms @ /accounts/index
    """
    title = 'Login/Registration'
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        return_user = authenticate(username=username, password=password)
        login(request, return_user)
        print(request.user.is_authenticated())
        return redirect('/')

    registration_form = UserRegisterForm(request.POST or None)
    print(request.user.is_authenticated())
    if registration_form.is_valid():
        user = registration_form.save(commit=False)
        password = registration_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('/')

    context = { 'login_form': login_form,
                'registration_form': registration_form, 
                'title': title, }

    return render(request, 'form.html', context=context)

def register_view(request):
    """
    Process post data to register a new account @ /accounts/users/new

    Registration includes fields: name, alias, email, 8-char password, password confirmation
    """
    pass
    # return render(request, 'form.html', {})

def login_view(request):
    """
    Process user login @ /accounts/users/login

    Login includes fields: Email, password
    """
    pass
    # return render(request, 'form.html', {})

def logout_view(request):
    """
    Process user logout, redirects to login/reg page @ accounts/users/logout
    """
    logout(request)
    return redirect('/')

def user_profile(request):
    """
    Render logged in user profile at /accounts/users/<id>

    Profile includes: Alias, name, email, total reviews, and list of reviews
    """
    pass
