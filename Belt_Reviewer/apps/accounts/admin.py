# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from .models import UserProfile


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user_id', 'user', 'name', 'email', 'count_reviews']
#     ordering = ['id',]
#     list_filter = ('count_reviews', )


# class ProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)