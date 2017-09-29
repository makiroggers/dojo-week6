# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import Http404, redirect, render, reverse
from django_tables2 import RequestConfig
from .forms import *
from .models import *
from .tables import *


def index(request):
    """
    Renders registration and login forms 
    """
    title = 'Login/Registration'
    login_form = UserLoginForm()
    registration_form = UserRegisterForm()
    context = {'login_form': login_form,
               'registration_form': registration_form,
               'title': 'title', }
    return render(request, 'form.html', context=context)


def register_view(request):
    """
    Process post data to register a new account 
    Registration includes fields: name, alias, email, 8-char password, password confirmation
    """
    title = 'Login/Registration'
    login_form = UserLoginForm()
    registration_form = UserRegisterForm(request.POST or None)
    if registration_form.is_valid():
        user = registration_form.save(commit=False)
        password = registration_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:accounts_index')
    context = {'login_form': login_form,
               'registration_form': registration_form,
               'title': title, }
    return render(request, 'form.html', context=context)


def login_view(request):
    """
    Process user login 
    Login includes fields: Email, password
    """
    title = 'Login/Registration'
    registration_form = UserRegisterForm()
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        try:
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            return_user = authenticate(username=username, password=password)
            login(request, return_user)
        except:
            raise Http404("This user does not exist.")
        return redirect('accounts:accounts_index')
    context = {'login_form': login_form,
               'registration_form': registration_form,
               'title': title, }
    return render(request, 'form.html', context=context)


def logout_view(request):
    """
    Process user logout, redirects to login/reg page 
    """
    logout(request)
    return redirect('accounts:accounts_index')


# def profile_view(request, user_id):
#     """
#     Render logged in user profile at /accounts/users/<id>
#     Profile includes: Alias, name, email, total reviews, and list of reviews
#     """
#     try:
#         user_id = User.objects.get(pk=user_id)
#         user_profile = UserProfile.objects.get(user_id=user_id)
#     except User.DoesNotExist:
#         raise Http404("User does not exist.")
#     return render(request, 'user_profile.html', {'user': user_id, 'user_profile': user_profile, })


# @login_required
# @transaction.atomic
# def profile_update(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, (
#                 'Your profile was successfully updated!'))
#             return redirect('accounts:update_profile')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.userprofile)
#     return render(request, 'user_edit.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

# def profile_list(request):
#     '''
#     queryset = UserProfile.objects.all()
#     table = SimpleTable(queryset)
#     '''
#     table = UserProfileTable(UserProfile.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'user_list.html', {'table': table})
