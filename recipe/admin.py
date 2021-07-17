"""Configure admin for Recipes App
"""
from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    """admin for Recipe model
    """
    model = Recipe


class CommentAdmin(admin.ModelAdmin):
    """admin for Comment model
    """
    model = Comment


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
