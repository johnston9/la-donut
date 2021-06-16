from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('update/<item_id>/', views.update_bag, name='update_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('remove/<item_id>/<item_size>/', views.remove_from_bag_sizes, name='remove_from_bag_sizes'),
    path('remove/<item_id>/<item_forsix>/', views.remove_from_bag_six, name='remove_from_bag_six'),
]
