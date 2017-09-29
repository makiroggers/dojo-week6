# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Trip, Traveler, Trip_Travelers


class TripAdmin(admin.ModelAdmin):
    model = Trip
    # list_display = ['title', 'author', 'created_at']
    # list_filter = ['author']
    # search_fields = ['title', 'author']


class TravelerAdmin(admin.ModelAdmin):
    model = Traveler
    # list_display = ['book', 'user', 'rating', 'review_text', 'updated_at']
    # list_filer = ['updated_at', 'user']
    # search_fields = ['review_text']


class TripTravelersAdmin(admin.ModelAdmin):
    model = Trip_Travelers
    # list_display = ['book', 'user', 'rating', 'review_text', 'updated_at']
    # list_filer = ['updated_at', 'user']
    # search_fields = ['review_text']

admin.site.register(Trip, TripAdmin)
admin.site.register(Traveler, TravelerAdmin)
admin.site.register(Trip_Travelers, TripTravelersAdmin)
