from django.urls import path
from hotel.views.Guest import views

urlpatterns = [
    path('list_guests', views.list_guests, name='list_guests'),
    ]