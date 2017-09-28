
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select
# from pagedown.widgets import PagedownWidget
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    # # book = forms.CharField(max_length=250, label='Title of Book', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # rating = forms.ChoiceField(choices=RATING_CHOICES, required=False)

    class Meta:
        model = Review
        fields = ['book',
                  'author_add',
                  'rating',
                  'review_text',]
        labels = {
            'book': 'Title of Book',
            'author_add': 'Author of Book',
            'rating': 'Your Rating',
            'review_text': 'Your Review',
        }
        widgets = {
            'book': forms.TextInput(attrs={'class': 'form-control'}),
            'author_add': forms.TextInput(attrs={'class': 'form-control'}),
            'review_text': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
