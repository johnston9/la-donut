"""Urls for the Product App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.view_item, name='view_item'),
    path('add/', views.add_product, name='add_product'),
]
