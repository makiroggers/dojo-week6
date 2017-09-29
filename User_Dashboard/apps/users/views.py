# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import *


def index(request):
    registration_form = UserRegistrationForm(request.POST or None)
    login_form = UserLoginForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    context = {
        'login_form': login_form,
        'registration_form': registration_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/index.html', context)

def login_view(request):
    response = "Placeholder to verify login_view creation."
    return HttpResponse(response)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    response = "Placeholder to verify register_view creation."
    return HttpResponse(response)

def user_wall(request):
    response = "Placeholder to verify user_wall creation."
    return HttpResponse(response)

def admin_edit_user(request):
    response = "Placeholder to verify admin_edit_user creation."
    return HttpResponse(response)

def user_edit_user(request):
    response = "Placeholder to verify user_edit_user creation."
    return HttpResponse(response)
