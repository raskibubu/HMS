from django.urls import path
from hotel.views.Payment import views

urlpatterns = [
    path('make_payment_now', views.create_payment, name='make_payment_now'),
    ]

