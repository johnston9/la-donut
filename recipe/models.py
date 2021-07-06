""" Models for the Recipe App
"""
from django.db import models
from profiles.models import UserProfile


class Recipe(models.Model):
    """Recipe Model for the Recipe App
    """

    title = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    is_vegan = models.BooleanField(default=False, null=True, blank=True)
    ingredients = models.TextField()
    preparation = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comments Model for the Recipe App
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    name = models.CharField(max_length=40)
    is_shop = models.BooleanField(default=False, null=True, blank=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
