# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='review_index'),
    url(r'^add/$', views.add_review, name='add_review'),
    url(r'^reviews/all/$', views.review_list, name='review_list'),
    url(r'^(?P<review_id>[0-9]+)/$', views.view_review, name='review_detail'),
    url(r'^books/all/$', views.book_list, name='book_list'),
    url(r'^books/(?P<book_id>[0-9]+)/$', views.view_book, name='book_detail'),
]
