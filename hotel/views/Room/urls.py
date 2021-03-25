from django.urls import path
from hotel.views.Room import views

urlpatterns = [
    path('create_room', views.create_room, name='create_room'),
    path('list_rooms', views.list_rooms, name='list_rooms'),
    path('change_room_type', views.change_room_type, name='change_room_type')
    ]
