# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='accounts_index'),
    # url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    # url(r'^register$', views.register, name='register'),
    # url(r'^success$', views.success, name='success'),
]
