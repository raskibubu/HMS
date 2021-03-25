from django.shortcuts import render

from hotel.service_provider import hms_service_provider
from hotel.dto.GuestDto import *


def create_guest_if_post_method(request):
    if request.method == 'POST':
        guest = CreateGuest()
        guest.guest_name = hms_service_provider.customer_management_service().get_customer_first_name(request.user.id)
        guest.guest_status = 'active'
        guest_id = hms_service_provider.customer_management_service().get_customer_id(request.user.id)
        guest.booking_id = hms_service_provider.booking_management_service().get_booking_id(guest_id)
        guest.room_number = hms_service_provider.booking_management_service().get_booking_room_number(guest_id)
        hms_service_provider.guest_management_service().create_guest(guest)


def list_guests(request):
    guests = hms_service_provider.guest_management_service().list_guests()
    context = {
        'guests': guests
    }
    return render(request, 'guest/listguests.html', context)
