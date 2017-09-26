# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
from django.db import models
import re
import bcrypt


class UserManager(models.Manager)

class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_Length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    objects = UserManager()

    def __str__(self):
        return self.email
"""
