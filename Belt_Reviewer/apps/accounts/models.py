# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

users = User.objects.all()

class UserProfile(models.Model):
    # users = User.objects.all()
    # print(users)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Alias', related_name='userprofile')
    name = models.CharField(max_length=100, blank=True)
    # username = models.CharField(verbose_name='Alias', max_length=45)
    email = models.EmailField(max_length=100)
    count_reviews = models.IntegerField(verbose_name='Number of Reviews', blank=True, null=True, default='0')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    AUTH_PROFILE_MODULE = 'app.UserProfile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
