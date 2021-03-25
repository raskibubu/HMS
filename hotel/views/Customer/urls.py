from django.urls import path
from hotel.views.Customer import views

urlpatterns = [
    path('register', views.create_customer, name='register'),
    path('list_customers', views.list_customers, name='list_customers')
    ]
