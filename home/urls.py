from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.home, name='home'),
    path('all/', views.all, name='all'),
    path('resize/', views.resize, name='resize'),
]
