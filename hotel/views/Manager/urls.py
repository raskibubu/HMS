from django.urls import path
from hotel.views.Manager import views

urlpatterns = [
    path('register', views.create_manager, name='register_manager'),
    ]
