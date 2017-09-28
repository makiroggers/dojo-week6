# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_tables2 as tables
from django_tables2 import A
from .models import Book, Review


class BooksTable(tables.Table):
    title = tables.LinkColumn('reviews:book_detail', text=lambda record: record.title, args=[A('pk')])

    class Meta:
        model = Book
        # name = tables.LinkColumn('title', args=[A('book_id')])
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('id', 'created_at', 'updated_at')

class ReviewsTable(tables.Table):
    class Meta:
        model = Review
        attrs = {'class': 'table table-striped table-hover'}
