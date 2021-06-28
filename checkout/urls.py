"""Create the urls for the Checkout App
"""
from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('extra_checkout_info/', views.extra_checkout_info,
         name='extra_checkout_info'),
    path('checkout_complete/<order_number>',
         views.checkout_complete, name='checkout_complete'),
    path('wh/', webhook, name='webhook'),
]
