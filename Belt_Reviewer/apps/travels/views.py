# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from .forms import *

def index(request):
    """
    This view will show a user dashboard featuring tables which display that user's trips, as well as the trips of other users with the option to join.
    URL ROUTE: /travels/
    """
    response = "Placeholder to verify travels app creation. (Index View)"
    return HttpResponse(response)


def add_trip(request):
    """
    This view displays a form for user's to add a new trip.
    URL ROUTE: /travels/add/
    """
    response = "Placeholder to verify travels app creation. (Add Trip View)"
    return HttpResponse(response)


def view_trip(request):
    """
    This view shows information about a given trip, including all of the users who will be traveling.
    URL ROUTE: /travels/destination/<id>
    """
    response = "Placeholder to verify travels app creation. (View Trip View)"
    return HttpResponse(response)
