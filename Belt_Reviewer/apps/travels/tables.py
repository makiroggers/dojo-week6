# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_tables2 as tables
from django_tables2 import A
from .models import *


class TripsTable(tables.Table):
    title = tables.LinkColumn('travels:trip_detail',
                              text=lambda record: record.title, args=[A('pk')])

    class Meta:
        model = Trip
        name = tables.LinkColumn('destination', args=[A('trip_id')])
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('id', 'created_at', 'updated_at')


# class ReviewsTable(tables.Table):
#     class Meta:
#         model = Review
#         attrs = {'class': 'table table-striped table-hover'}
