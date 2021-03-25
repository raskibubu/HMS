from django.http import HttpRequest
from django.shortcuts import redirect, render
from hotel.service_provider import hms_service_provider
from hotel.dto.BookingsDto import *
from hotel.dto.RoomsDto import *
from hotel.dto.PaymentDto import *

room_types = {
    'Basic': 5000,
    'Deluxe': 10000,
    'Mega-Deluxe': 15000,
    'Presidential': 30000
}


def __get_room_amount_by_room_type(room_type: str):
    for room in room_types:
        if room == room_type:
            result = room_types[room]
            return result
    return None


def __get_attribute_from_request(request: HttpRequest):
    make_booking_dto = CreateBooking()
    make_booking_dto.room_type = request.POST['room_type']
    make_booking_dto.check_in = request.POST['check_in']
    make_booking_dto.check_out = request.POST['check_out']
    make_booking_dto.payment_type = request.POST['payment_type']
    return make_booking_dto


def list_bookings(request):
    bookings = hms_service_provider.booking_management_service().list_booking()
    context = {
        'bookings': bookings

    }
    return render(request, 'booking/list.html', context)


def get_booking_if_post_method(request, context):
    if request.method == 'POST':
        booking_request = __get_attribute_from_request(request)
        if booking_request:
            confirm_date = __check_in_check_out_processor(booking_request.check_in, booking_request.check_out)

            if confirm_date is True:
                booking = __check_if_any_active_booking(str(booking_request.check_in),
                                                        str(booking_request.check_out), booking_request.room_type)
                if booking is None:
                    booking_request.payment_status = 'not paid'
                    booking_request.number_of_rooms = 1
                    booking_request.booking_reference = __booking_reference(booking_request.payment_status)
                    booking_request.room_type = __get_room_type(booking_request.room_type)
                    room_details = __get_room_type(booking_request.room_type[0])
                    booking_request.room_type = room_details[0]
                    booking_request.room_number = room_details[1]
                    booking_request.room_id = booking_request.room_number
                    booking_request.payment_id = str(__payment_id(booking_request.booking_reference))
                    booking_request.customer_id = hms_service_provider.customer_management_service().get_customer_id(
                        request.user.id)
                    booking_request.booking_amount = int(
                        __get_room_amount_by_room_type(booking_request.room_type)) * int(
                        __num_of_days(str(booking_request.check_in), str(booking_request.check_out)))
                    booking_request.payment_type = booking_request.payment_type
                    if booking_request.payment_type == 'Pay Now':
                        hms_service_provider.booking_management_service().create_booking(booking_request)
                        context['saved'] = True
                else:
                    context['saved'] = False
            else:
                context['saved'] = False
        else:
            context['saved'] = False
    else:
        context['saved'] = False


def create_booking(request):
    context = {

    }
    get_booking_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('make_payment_now')
    return render(request, 'booking/createbooking.html', context)


def __get_room_number() -> ListRooms:
    rooms: list = hms_service_provider.room_management_service().list_rooms()
    rooms_to_choose = []
    for room in rooms:
        if room.room_status == 'unbooked':
            rooms_to_choose.append(room.room_number)
        return rooms_to_choose[0]


def __get_room_type(room_type: str) -> list:
    rooms: list = hms_service_provider.room_management_service().list_rooms()
    rooms_to_choose = []
    rooms_to_choose_number = []
    for room in rooms:
        if room.room_type == room_type:
            rooms_to_choose.append(room.room_type)
            rooms_to_choose_number.append(room.room_number)
    room_details: list = [rooms_to_choose[0], rooms_to_choose_number[0]]
    return room_details


def __check_in_check_out_processor(check_in: date, check_out: date):
    if check_in < check_out:
        return True
    elif check_in == check_out:
        return False
    elif check_in > check_out:
        return False


def __num_of_days(check_in: str, check_out: str):
    check_in_list = []
    check_out_list = []
    a = check_in.split('-')
    b = check_out.split('-')
    for i in a:
        check_in_list.append(int(i))
    for i in b:
        check_out_list.append(int(i))
    date1 = date(check_in_list[0], check_in_list[1], check_in_list[2])
    date2 = date(check_out_list[0], check_out_list[1], check_out_list[2])
    answer = (date2 - date1)
    return answer.days


def __booking_reference(reference: str):
    import uuid
    reference = uuid.uuid4()
    reference2 = reference.node
    return str(reference2)


def __check_if_any_active_booking(check_in: str, check_out: str, room_type: str):
    bookings: list = hms_service_provider.booking_management_service().list_booking_by_check_in_check_out(check_in,
                                                                                                          check_out,
                                                                                                          room_type,
                                                                                                          )
    for booking in bookings:
        if booking:
            return booking
        else:
            return False


def __payment_id(reference2: str):
    import uuid
    reference = uuid.uuid4()
    reference2 = reference.node
    return reference2


def __get_attribute_from_request_for_payment_pay_now(request: HttpRequest):
    make_payment_dto = CreatePayment()
    make_payment_dto.amount = request.POST['amount']
    return make_payment_dto
