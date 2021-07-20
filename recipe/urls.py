"""Urls for the Recipe model
"""
from django.urls import path
from . import views

urlpatterns = [
    path('recipe', views.recipe, name='recipe'),
    path('get_recipe/<int:recipe_id>/', views.get_recipe, name='get_recipe'),
    path('latest_recipe/', views.latest_recipe, name='latest_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe,
         name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe,
         name='delete_recipe'),
    path('chat/', views.chat, name='chat'),
    path('cut_comment/<int:comment_id>/', views.cut_comment,
         name='cut_comment'),
]
