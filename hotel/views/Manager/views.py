from django.http import HttpRequest
from django.shortcuts import redirect, render
from hotel.service_provider import hms_service_provider
from hotel.dto.ManagerDto import *


def create_manager(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, '', context)


def list_managers(request):
    managers = hms_service_provider.manager_management_service().create_manager()
    context = {
        'managers': managers
    }
    return render(request, 'room/createroom.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            manager = __get_attribute_from_request(request)
            if manager.password == manager.confirm_password:
                hms_service_provider.manager_management_service().create_manager(manager)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request(request: HttpRequest):
    register_manager_dto = RegisterManager()
    register_manager_dto.username = request.POST['username']
    register_manager_dto.first_name = request.POST['first_name']
    register_manager_dto.last_name = request.POST['last_name']
    register_manager_dto.email = request.POST['email']
    register_manager_dto.address = request.POST['address']
    register_manager_dto.date_of_birth = request.POST['date_of_birth']
    register_manager_dto.phone_number = request.POST['phone_number']
    register_manager_dto.password = request.POST['password']
    register_manager_dto.confirm_password = request.POST['confirm_password']
    return register_manager_dto
