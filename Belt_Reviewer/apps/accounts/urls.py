# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='accounts_index'),
    url(r'^users/login$', views.login_view, name='login'),
    url(r'^users/logout$', views.logout_view, name='logout'),
    url(r'^users/new$', views.register_view, name='register'),
    url(r'^users/profile/(?P<user_id>\d+)$', views.profile_view, name='profile'),
    url(r'^users/edit$', views.profile_update, name='update_profile'),
    url(r'^users/list$', views.profile_list, name='users_list')
]
