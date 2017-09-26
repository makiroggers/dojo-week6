# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for the front page of the website.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    num_books_with_word = Book.objects.filter(title__icontains='the').count()

    return render(request, 'catalog/index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_genres': num_genres,
                                                  'num_books_with_word': num_books_with_word, })

class BookListView(generic.ListView):
    model = Book
    # Designated name for the list as a template variable
    context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # Specify a different template name/location
    template_name = 'books/my_arbitrary_template_name_list.html'

    def get_queryset(self):
        # Get 5 books containing the title war
        # return Book.objects.filter(title__icontains='the')[:5]
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 2

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'my_author_list'
    paginate_by = 2
    
    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author

    # def get_queryset(self):
        # return Author.objects.get(pk)
        

"""
As a function:

def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
"""
