from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    # path('shop_menu', views.shop_menu, name='shop_menu'),
    path('<product_id>', views.view_item, name='view_item'),
]
