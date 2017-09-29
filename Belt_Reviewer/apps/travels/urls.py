# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='travel_index'),
    url(r'^add/$', views.add_trip, name='add_trip'),
    url(r'^destination/(?P<trip_id>[0-9]+)/$', views.view_trip, name='trip_detail'), 
]
