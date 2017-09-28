# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django_tables2 import RequestConfig
from .models import Book, Review
from .tables import BooksTable, ReviewsTable
from .forms import ReviewForm


def index(request):
    """
    User dashboard page that shows latest reviews and list of all reviews
    @ /reviews/books/index
    """
    response = "Placeholder to verify reviews app creation."
    return HttpResponse(response)

def review_list(request):
    table = ReviewsTable(Review.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'reviews/review_list.html', {'table': table})

    """
    all_reviews_list = Review.objects.all()
    latest_reviews_list = Review.objects.order_by('-created_at')[:3]
    context = {
        'all_reviews': all_reviews_list, 
        'latest_reviews': latest_reviews_list
    }
    return render(request, 'reviews/review_list.html', context)
    """

def book_list(request):
    all_books_list = Book.objects.all()
    table = BooksTable(Book.objects.all())
    context = {
        'all_books_list': all_books_list,
        'table': table,
    }
    RequestConfig(request).configure(table)
    return render(request, 'reviews/book_list.html', context)

@login_required(login_url='/')
def add_review(request):
    """
    Shows form to add a new book and/or new book review @ reviews/books/new/
    Includes: book title, author (choose from list AND add new), review description, star rating
    """
    review_form = ReviewForm(request.POST or None)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = get_object_or_404(User, pk=request.user.id)
        review_form.save()
        
    return render(request, 'reviews/review_new.html', {'review_form': review_form,})

def view_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def view_book(request, book_id):
    """
    Displays individual book details at reviews/books/<id> & allows user to add/delete a review for the given book
    Includes: title, author, reviews
    """
    try:
        book_id = Book.objects.get(pk=book_id)
        print(book_id)
        reviews = Review.objects.all()
        print(reviews)
        review_form = ReviewForm(request.POST or None)
    except:
        print("Didn't work")
    # book = get_object_or_404(Book, pk=book_id)
    return render(request, 'reviews/book_detail.html', {'book': book_id, 'review': reviews, 'form': review_form})


def delete_review(request):
    """
    Processes logged in user deleting their own review @ reviews/books/delete
    """
    pass


def post_review(request):
    """
    Processes post data for a new review @ reviews/books/post
    """
    pass
