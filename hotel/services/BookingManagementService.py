from abc import abstractmethod, ABCMeta
from typing import List
from hotel.repository.BookingRepository import BookingRepository
from hotel.dto.BookingsDto import *


class BookingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_booking(self, model: CreateBooking):
        raise NotImplementedError

    @abstractmethod
    def list_booking(self) -> List[ListBookings]:
        raise NotImplementedError

    @abstractmethod
    def get_customer_details_by_customer_id(self, customer_id: int) -> BookingDetails:
        raise NotImplementedError

    @abstractmethod
    def get_booking_id(self, user_id: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_booking_room_number(self, user_id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def list_booking_by_check_in_check_out(self, check_in: str, check_out: str, room_type: str) -> List[ListBookings]:
        raise NotImplementedError

    @abstractmethod
    def get_booking_details_by_payment_type(self, payment_type: str) -> CreateBooking:
        raise NotImplementedError

    @abstractmethod
    def get_booking_by_booking_id(self, booking_id: int) -> CreateBooking:
        raise NotImplementedError


class DefaultBookingManagementService(BookingManagementService):
    repository: BookingRepository

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def create_booking(self, model: CreateBooking):
        return self.repository.create_booking(model)

    def list_booking(self) -> List[ListBookings]:
        return self.repository.list_booking()

    def get_customer_details_by_customer_id(self, customer_id: int) -> BookingDetails:
        return self.repository.get_customer_details_by_customer_id(customer_id)

    def get_booking_id(self, user_id: int) -> str:
        return self.repository.get_booking_id(user_id)

    def get_booking_room_number(self, user_id: int) -> int:
        return self.repository.get_booking_room_number(user_id)

    def list_booking_by_check_in_check_out(self, check_in: str, check_out: str, room_type: str) -> List[ListBookings]:
        return self.repository.list_booking_by_check_in_check_out(check_in, check_out, room_type)

    def get_booking_details_by_payment_type(self, payment_type: str) -> CreateBooking:
        return self.repository.get_booking_details_by_payment_type(payment_type)

    def get_booking_by_booking_id(self, booking_id: int) -> CreateBooking:
        raise self.repository.get_booking_by_booking_id(booking_id)
