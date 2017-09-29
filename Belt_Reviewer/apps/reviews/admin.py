# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Review

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author']
    search_fields = ['title', 'author']

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['book', 'user', 'rating', 'review_text', 'updated_at']
    list_filer = ['updated_at', 'user']
    search_fields = ['review_text']

# admin.site.register(Book, BookAdmin)
# admin.site.register(Review, ReviewAdmin)
