# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    """
    User dashboard page that shows latest reviews and list of all reviews
    @ /reviews/books/index
    """
    response = "Placeholder to verify reviews app creation."
    return HttpResponse(response)


def new_review(request):
    """
    Shows form to add a new book and/or new book review @ reviews/books/new/
    Includes: book title, author (choose from list AND add new), review description, star rating
    """
    pass


def view_book(request):
    """
    Displays individual book details at reviews/books/<id> & allows user to add/delete a review for the given book
    Includes: title, author, reviews
    """
    pass


def delete_review(request):
    """
    Processes logged in user deleting their own review @ reviews/books/delete
    """


def post_review(request):
    """
    Processes post data for a new review @ reviews/books/post
    """
    pass
