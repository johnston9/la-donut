from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
