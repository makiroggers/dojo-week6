# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm, Textarea, TextInput, DateInput
from .models import *


class TripForm(forms.ModelForm):
    """
    This form gathers information from a user about their trip.
    """
    
    class Meta:
        model = Trip
        fields = ['destination',
                  'plans',
                  'travel_from', 
                  'travel_to', ]
        labels = {'destination': 'Travel Destination',
                  'plans': 'Plan Description',
                  'travel_from': 'Travel Date From',
                  'travel_to': 'Travel Date To', }
        widgets = {'destination': forms.TextInput(attrs={'class': 'form-control'}),
                   'plans': forms.TextInput(attrs={'class': 'form-control'}),
                   'travel_from': forms.DateInput(attrs={'class': 'form-control'}),
                   'travel_to': forms.DateInput(attrs={'class': 'form-control'}), }
