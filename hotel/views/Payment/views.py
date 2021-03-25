from django.shortcuts import redirect, render

from hotel.models import Payment
from django.http import HttpRequest
from hotel.service_provider import hms_service_provider
from hotel.dto.PaymentDto import *


def __get_attribute_from_request_for_payment_pay_now(request: HttpRequest):
    make_payment_dto = CreatePayment()
    make_payment_dto.amount = request.POST['amount']
    return make_payment_dto


def __make_payment_pay_now_if_post_method(request, context):
    if request.method == 'POST':
        try:
            payment = __get_attribute_from_request_for_payment_pay_now(request)
            if payment:

        #
        #     if payment:
        #         payment.booking_id = hms_service_provider.booking_management_service().get_booking_id()
        #
        #         booking_id = hms_service_provider.booking_management_service().get_booking_id(request.user.id)
        #         booking = hms_service_provider.booking_management_service().get_booking_by_booking_id(booking_id)
        #         if booking.booking_amount > payment.amount:
        #             payment.booking_id = hms_service_provider.booking_management_service().get_booking_id(
        #                 request.user.id)
        #             payment.customer_id = hms_service_provider.customer_management_service().get_customer_id(
        #                 request.user.id)
        #             payment.payment_status = booking.payment_status
        #             payment.payment_type = booking.payment_type
        #             payment.balance = booking.booking_amount
        #
        #         if payment.amount > booking.booking_amount:
        #             booking.booking_amount -= payment.amount
        #         elif payment.amount == booking.booking_amount:
        #             booking.booking_amount -= payment.amount
        #         elif payment.amount < booking.booking_amount:
        #             payment.amount = 0
        #     else:
        #         context['saved'] = False
        # except Payment.DoesNotExist as e:
        #     raise e


def create_payment(request):
    context = {

    }
    __make_payment_pay_now_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('profile')
    return render(request, 'payment/paynow.html', context)
