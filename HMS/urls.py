"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hotel.views.Customer import views
from hotel.views.Home import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name='home'),
    path('customer/', include('hotel.views.Customer.urls')),
    path('manager/', include('hotel.views.Manager.urls')),
    path('room/', include('hotel.views.Room.urls')),
    path('login/', include('hotel.views.login.urls')),
    path('booking/', include('hotel.views.Booking.urls')),
    path('guest/', include('hotel.views.Guest.urls')),
    path('payment/', include('hotel.views.Payment.urls'))

]
