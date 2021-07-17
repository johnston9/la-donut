"""Configure admin for Profiles App
"""
from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """admin for UserProfile model
    """
    model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
