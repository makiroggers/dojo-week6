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
    # Queries and context
    title = 'My Travel Dashboard'
    current_user = request.user.id
    all_trips = Trip.objects.all()
    all_travel_table = AllTripsTable(all_trips)
    my_trips = Trip.objects.filter(travelers=current_user)
    my_travel_table = MyTripsTable(my_trips)
    
    context = {
        'title': title,
        'current_user': request.user,
        'all_trips': all_trips,
        'my_trips': my_trips,
        'my_travel_table': my_travel_table,
        'all_travel_table': all_travel_table,
    }
    # Debug statements
    print(current_user)
    print(my_trips)
    print(all_trips)

    RequestConfig(request).configure(all_travel_table)
    RequestConfig(request).configure(my_travel_table)
    return render(request, 'travels/index.html', context)



def add_trip(request):
    """
    This view displays a form for user's to add a new trip.
    URL ROUTE: /travels/add/
    """

    title = 'Add a New Trip'
    trip_form = TripForm(request.POST or None)

    try:
        trip_form.save(request.POST)
        print(trip_form.cleaned_data)
        destination = trip_form.cleaned_data.get('destination')
        plans = trip_form.cleaned_data.get('plans')
        travel_from = trip_form.cleaned_data.get('travel_from')
        travel_to = trip_form.cleaned_data.get('travel_to')
        messages.success(request, ('Your trip was added!'))
        return redirect('travels:travel_index')
    except:
        print('Something went wrong.')
    context = {
        'title': title,
        'trip_form': trip_form,
    }
    return render(request, 'travels/add_trip.html', context)


def view_trip(request, trip_id):
    """
    This view shows information about a given trip, including all of the users who will be traveling.
    URL ROUTE: /travels/destination/<id>
    """
    trip = Trip.objects.get(pk=trip_id)
    title = trip.destination

    # Update query to be dynamic, placeholder currently
    first_traveler = 'Maki'
    other_travelers = ['Josh', 'Susan', 'Michael']

    context = {
        'title': title,
        'trip': trip,
        'first_traveler': first_traveler,
        'other_travelers': other_travelers,
    }
    return render(request, 'travels/trip_detail.html', context)
