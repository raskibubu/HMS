from django.http import HttpRequest
from django.shortcuts import redirect, render
from hotel.service_provider import hms_service_provider
from hotel.dto.RoomsDto import *
from hotel.models import Rooms
import random


def __get_attribute_from_request(request: HttpRequest):
    create_room_dto = CreateRoom()
    create_room_dto.room_type = request.POST['room_type']
    create_room_dto.room_number = request.POST['room_number']
    return create_room_dto


def create_room(request):
    context = {

    }
    __create_room_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('home')
    return render(request, 'room/createroom.html', context)


def change_room_type(request):
    context = {

    }
    __change_room_type_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('home')
    return render(request, 'room/changeroomtype.html', context)


def list_rooms(request):
    rooms = hms_service_provider.room_management_service().list_rooms()

    context = {
        'rooms': rooms
    }
    return render(request, 'room/list.html', context)


def __create_room_if_post_method(request, context):
    if request.method == 'POST':
        try:
            room = __get_attribute_from_request(request)
            if room:
                room.room_type = __get_room_type(room.room_type)
                room.room_id = room.room_number
                room.room_number = room.room_number
                room.room_status = 'unbooked'
                hms_service_provider.room_management_service().create_room(room)
                context['saved'] = True
            else:
                context['saved'] = False
        except Rooms.DoesNotExist as e:
            raise e


def __get_room_type(room_type: str):
    room_types = {
        'Basic': 'Basic Room',
        'Deluxe': 'Deluxe Room',
        'Mega-Deluxe': 'Mega-Deluxe Room',
        'Presidential': 'Presidential Room'

    }

    for room in room_types:
        if room == room_type:
            return room
    return None


def __get_attribute_from_request_for_room_type(request):
    change_room_type_dto = ChangeRoomType()
    change_room_type_dto.room_number = request.POST['room_number']
    change_room_type_dto.room_type = request.POST['room_type']
    return change_room_type_dto


def __change_room_type_if_post_method(request, context):
    if request.method == 'POST':
        transaction = __get_attribute_from_request_for_room_type(request)
        room = hms_service_provider.room_management_service().get_room_by_room_number(transaction.room_number)
        if room:
            room.room_type = transaction.room_type
            hms_service_provider.room_management_service().change_room_type(room)
            context['saved'] = True
        else:
            context['saved'] = False
