from abc import abstractmethod, ABCMeta
from typing import List

from hotel.models import Guest
from hotel.dto.GuestDto import *


class GuestRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_guest(self, model: CreateGuest):
        raise NotImplementedError

    @abstractmethod
    def change_guest_status(self, model: ChangeGuestStatus):
        raise NotImplementedError

    @abstractmethod
    def list_guests(self) -> List[ListGuests]:
        raise NotImplementedError


class DjangoORMAGuestRepository(GuestRepository):
    def create_guest(self, model: CreateGuest):
        guest = Guest()
        guest.name = model.guest_name
        guest.room_id = model.room_number
        guest.status = model.guest_status
        guest.booking_id = model.booking_id
        guest.save()

    def change_guest_status(self, model: ChangeGuestStatus):
        guest = Guest.objects.get(room__room_number=model.room_number)
        guest.status = model.guest_status
        guest.save()

    def list_guests(self) -> List[ListGuests]:
        guests = list(Guest.objects.values('name', 'booking_id', 'room_id', 'status'))
        results: List[ListGuests] = []
        for guest in guests:
            item = ListGuests()
            item.room_number = guest['room_id']
            item.booking_id = guest['booking_id']
            item.guest_name = guest['name']
            item.guest_status = guest['status']
            results.append(item)
        return results
