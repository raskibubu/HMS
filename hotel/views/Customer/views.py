from django.http import HttpRequest
from django.shortcuts import redirect, render
from hotel.service_provider import hms_service_provider
from hotel.dto.CustomerDto import *


def create_customer(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'customer/register.html', context)


def list_customers(request):
    customers = hms_service_provider.customer_management_service().list_customers()
    context = {
        'customers': customers
    }
    return render(request, 'customer/list.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            customer = __get_attribute_from_request(request)
            if customer.password == customer.confirm_password:
                hms_service_provider.customer_management_service().create_customer(customer)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request(request: HttpRequest):
    register_customer_dto = RegisterCustomer()
    register_customer_dto.username = request.POST['username']
    register_customer_dto.first_name = request.POST['first_name']
    register_customer_dto.last_name = request.POST['last_name']
    register_customer_dto.email = request.POST['email']
    register_customer_dto.address = request.POST['address']
    register_customer_dto.date_of_birth = request.POST['date_of_birth']
    register_customer_dto.phone_number = request.POST['phone_number']
    register_customer_dto.password = request.POST['password']
    register_customer_dto.confirm_password = request.POST['confirm_password']
    return register_customer_dto
