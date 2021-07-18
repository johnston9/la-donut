"""urls for Home App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('all/', views.all, name='all'),
    path('resize/', views.resize, name='resize'),
    path('delivery/', views.delivery, name='delivery'),
]
