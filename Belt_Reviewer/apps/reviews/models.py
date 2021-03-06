# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_init
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
import numpy as np


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(verbose_name='Date Added', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Last Updated', blank=True, null=True, auto_now=True)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Review(models.Model):
    # RATING_CHOICES = [
    #     (1, 1),
    #     (2, 2),
    #     (3, 3),
    #     (4, 4),
    #     (5, 5),
    # ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Add author dropdown
    author_add = models.CharField(max_length=100, verbose_name='Author of Book')
    review_text = models.TextField(max_length=1000)
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Date Added', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Last Updated', blank=True, null=True, auto_now=True)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def get_absolute_url(self):
        """
        Returns the url to access a particular review instance.
        """
        return reverse('review_detail', args=[str(self.id)])

    # @receiver(pre_init, sender=User)
    # def load_book_detail_review(sender, instance, book, **kwargs):
    #     instance.userprofile.save()

    def __str__(self):
        return self.book.title
