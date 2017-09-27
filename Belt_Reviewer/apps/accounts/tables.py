# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_tables2 as tables
from .models import UserProfile


class UserProfileTable(tables.Table):
    class Meta:
        model = UserProfile
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('id', 'created_at', 'updated_at')
