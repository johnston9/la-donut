"""Urls for the Product App
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.view_item, name='view_item'),
    path('add/', views.add_product, name='add_product'),
    path('price_size/<int:product_id>', views.price_size, name='price_size'),
    path('cost_forsix/<int:product_id>', views.cost_forsix, name='cost_forsix'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('sizeprice_edit/<int:product_id>/', views.sizeprice_edit, name='sizeprice_edit'),
    path('forsixprice_edit/<int:product_id>/', views.forsixprice_edit, name='forsixprice_edit'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
