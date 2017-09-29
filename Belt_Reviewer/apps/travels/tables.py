# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_tables2 as tables
from django_tables2 import A
from .models import *


class MyTripsTable(tables.Table):
    destination = tables.LinkColumn('travels:trip_detail',
                                    text=lambda record: record.destination, args=[A('pk')])

    class Meta:
        model = Trip
        name = tables.LinkColumn('destination', args=[A('trip_id')])
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('created_at', 'updated_at')
        sequence = ('id', 'destination', 'travel_from', 'travel_to', '...')

class AllTripsTable(tables.Table):
    destination = tables.LinkColumn('travels:trip_detail',
                              text=lambda record: record.destination, args=[A('pk')])
    join_trip = tables.TemplateColumn('<a href="URL_TO_JOIN_TRIP">Join</a>')


    class Meta:
        model = Trip
        name = tables.LinkColumn('destination', args=[A('trip_id')])
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('created_at', 'updated_at')
        sequence = ('id', 'destination', 'travel_from', 'travel_to', '...')



# class ReviewsTable(tables.Table):
#     class Meta:
#         model = Review
#         attrs = {'class': 'table table-striped table-hover'}
