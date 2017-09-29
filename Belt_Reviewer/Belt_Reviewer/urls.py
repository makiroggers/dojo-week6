# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from apps.accounts.views import index, login_view, register_view, logout_view

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^users/', include('apps.accounts.urls', namespace='users', app_name='apps.accounts')),
    # url(r'^reviews/', include('apps.reviews.urls', namespace='reviews', app_name='apps.reviews')),
    url(r'^travels/', include('apps.travels.urls', namespace='travels', app_name='apps.travels')),
    url(r'^$', RedirectView.as_view(url='/travels/', permanent=False)),
]
