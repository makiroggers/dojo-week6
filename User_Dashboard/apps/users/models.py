# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone

import django_tables2 as tables


class UserProfile(models.Model):
    """
    A simple user profile model class.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username', related_name='userprofile')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    AUTH_PROFILE_MODULE = 'app.UserProfile'

    # Metadata
    class Meta:
        ordering = ["-created_at"]

    # Methods
    def get_absolute_url(self):
        """
         Returns the url to access a particular instance of UserProfile.
         """
        return reverse('edit', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the UserProfile object (in Admin site etc.)
        """
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

'''
class Message(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    # Fields
    my_field_name = models.CharField(
        max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
'''
