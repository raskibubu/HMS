from abc import abstractmethod, ABCMeta
from typing import List
from hotel.repository.GuestRepository import GuestRepository
from hotel.dto.GuestDto import *


class GuestManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_guest(self, model: CreateGuest):
        raise NotImplementedError

    @abstractmethod
    def change_guest_status(self, model: ChangeGuestStatus):
        raise NotImplementedError

    @abstractmethod
    def list_guests(self) -> List[ListGuests]:
        raise NotImplementedError


class DefaultGuestManagementService(GuestManagementService):
    repository: GuestRepository

    def __init__(self, repository: GuestRepository):
        self.repository = repository

    def create_guest(self, model: CreateGuest):
        self.repository.create_guest(model)

    def change_guest_status(self, model: ChangeGuestStatus):
        self.repository.change_guest_status(model)

    def list_guests(self) -> List[ListGuests]:
        self.repository.list_guests()
