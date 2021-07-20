""" Models for the Recipe App
"""
from django.db import models
from profiles.models import UserProfile


class Recipe(models.Model):
    """Recipe Model for the Recipe App
    """

    title = models.CharField(max_length=254, default="", null=False,
                             blank=False)
    description = models.TextField(default="", null=False, blank=False)
    prep_time = models.CharField(max_length=100, default="", null=False,
                                 blank=False)
    cook_time = models.CharField(max_length=100, default="", null=False,
                                 blank=False)
    serves = models.CharField(max_length=100, default="", null=False,
                              blank=False)
    image = models.ImageField(null=True, blank=True)
    is_vegan = models.BooleanField(default=False, null=True, blank=True)
    ingredient1 = models.CharField(max_length=100, default="", null=False,
                                   blank=False)
    ingredient2 = models.CharField(max_length=100, default="", null=False,
                                   blank=False)
    ingredient3 = models.CharField(max_length=100, default="", null=False,
                                   blank=False)
    ingredient4 = models.CharField(max_length=100, default="", null=False,
                                   blank=False)
    ingredient5 = models.CharField(max_length=100, default="", null=False,
                                   blank=False)
    ingredient6 = models.CharField(max_length=100, default="", blank=True)
    ingredient7 = models.CharField(max_length=100, default="", blank=True)
    ingredient8 = models.CharField(max_length=100, default="", blank=True)
    ingredient9 = models.CharField(max_length=100, default="", blank=True)
    ingredient10 = models.CharField(max_length=100, default="", blank=True)

    step1 = models.TextField(default="", null=False, blank=False)
    step2 = models.TextField(default="", null=False, blank=False)
    step3 = models.TextField(default="", null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comments Model for the Recipe App
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    is_shop = models.BooleanField(default=False, null=True, blank=True)
    comment = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
