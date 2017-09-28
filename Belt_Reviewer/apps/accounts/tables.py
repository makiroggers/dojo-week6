# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_tables2 import A
import django_tables2 as tables
from .models import UserProfile


class UserProfileTable(tables.Table):
    alias = tables.LinkColumn('accounts:profile', text=lambda record: record.user, args=[A('pk')])

    class Meta:
        model = UserProfile
        attrs = {'class': 'table table-striped table-hover'}
        include = ('alias')
        exclude = ('user', 'id', 'created_at', 'updated_at')
        sequence = ('alias', 'name', 'email', 'count_reviews', '...')
