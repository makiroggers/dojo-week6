# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    response = "Placeholder to verify app index creation."
    return HttpResponse(response)

def user_dashboard(request):
    response = "Placeholder to verify user dashboard creation."
    return HttpResponse(response)

def admin_dashboard(request):
    response = "Placeholder to verify admin dashboard creation."
    return HttpResponse(response)
