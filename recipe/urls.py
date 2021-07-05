"""Urls for the Recipe model
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_comment/', views.add_comment, name='add_comment'),
]
