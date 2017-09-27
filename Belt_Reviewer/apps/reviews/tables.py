# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_tables2 as tables
from .models import Book, Review


class BooksTable(tables.Table):
    class Meta:
        model = Book
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('id', 'created_at', 'updated_at')

class ReviewsTable(tables.Table):
    class Meta:
        model = Review
        attrs = {'class': 'table table-striped table-hover'}
