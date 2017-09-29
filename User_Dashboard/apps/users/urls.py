# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.index, name='register'),
    url(r'^show/(?P<user_id>\d+)$', views.user_wall, name='user_wall'),
    url(r'^edit/(?P<user_id>\d+)$', views.admin_edit_user, name='admin_edit_user'),
    url(r'^edit$', views.user_edit_user, name='user_edit_user'),
]
