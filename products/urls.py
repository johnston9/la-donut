"""Urls for the Product App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.view_item, name='view_item'),
    path('add/', views.add_product, name='add_product'),
    path('add_size/<product_id>', views.add_size, name='add_size'),
    path('add_forsix/<product_id>', views.add_forsix, name='add_forsix')
]
