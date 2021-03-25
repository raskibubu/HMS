from django.urls import path
from hotel.views.Booking import views

urlpatterns = [
    path('create_booking', views.create_booking, name='create_booking'),
    path('list_booking', views.list_bookings, name='list_bookings')
    ]
