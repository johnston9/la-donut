"""Urls for the Recipe model
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('get_recipe/<int:recipe_id>/', views.get_recipe, name='get_recipe'),
    path('latest_recipe/', views.latest_recipe, name='latest_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('delete_recipe/recipe_id/', views.delete_recipe, name='delete_recipe'),
    path('chat/', views.chat, name='chat'),
]
