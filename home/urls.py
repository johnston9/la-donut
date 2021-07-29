"""urls for Home App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resize/', views.resize, name='resize'),
    path('delivery/', views.delivery, name='delivery'),
]
