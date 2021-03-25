from abc import abstractmethod, ABCMeta
from typing import List

from hotel.models import Booking, Customer
from hotel.dto.BookingsDto import *


class BookingRepository(metaclass=ABCMeta):
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


class DjangoORMABookingRepository(BookingRepository):
    def create_booking(self, model: CreateBooking):
        booking = Booking()
        booking.customer_id = model.customer_id
        booking.booking_amount = model.booking_amount
        booking.payment_id = model.payment_id
        booking.payment_status = model.payment_status
        booking.booking_reference = model.booking_reference
        booking.number_of_rooms = model.number_of_rooms
        booking.room_id = model.room_id
        booking.room_type = model.room_type
        booking.check_in = model.check_in
        booking.check_out = model.check_out
        booking.save()

    def list_booking(self) -> List[ListBookings]:
        bookings = list(
            Booking.objects.values('customer_id', 'booking_reference', 'check_in', 'check_out',
                                   'room__room_number',
                                   'room__room_type', 'payment_status'))
        results: List[ListBookings] = []
        for booking in bookings:
            item = ListBookings()
            item.customer_id = booking['customer_id']
            item.booking_reference = booking['booking_reference']
            item.check_out = booking['check_in']
            item.check_in = booking['check_out']
            item.room_number = booking['room__room_number']
            item.room_type = booking['room__room_type']
            item.payment_status = booking['payment_status']
            results.append(item)
        return results

    def get_customer_details_by_customer_id(self, customer_id: int) -> BookingDetails:
        item = BookingDetails()
        customer = Customer.objects.get(user_id=customer_id)
        booking = Booking.objects.get(room__booking__customer_id=customer_id)
        item.customer_id = customer.user.id
        item.room_number = booking.room.room_number
        item.room_type = booking.room.room_type
        item.booking_reference = booking.booking_reference
        item.payment_status = booking.payment_status
        item.check_in = booking.check_in
        item.check_out = booking.check_out
        return item

    def get_booking_id(self, user_id: int) -> str:
        try:
            booking = Booking.objects.values('booking_reference]').get(customer_id=user_id)
            item = BookingID()
            item.booking_reference = booking['booking_reference']
            return str(item.booking_reference)
        except Booking.DoesNotExist as e:
            raise e

    def get_booking_room_number(self, user_id: int) -> int:
        try:
            booking = Booking.objects.values('room__room_id').get(customer_id=user_id)
            item = BookedRoomID()
            item.room_id = booking['room__room_id']
            return int(item.room_id)
        except Booking.DoesNotExist as e:
            raise e

    def list_booking_by_check_in_check_out(self, check_in: str, check_out: str, room_type: str) -> List[ListBookings]:
        bookings = list(
            Booking.objects.values('payment_id', 'payment_type', 'name', 'room_id', 'customer_id', 'room_type',
                                   'booking_reference', 'check_in', 'check_out', 'number_of_rooms', ).filter(
                check_out=check_out,
                check_in=check_in).filter(
                room_type=room_type))
        results: List[ListBookings] = []

        for booking in bookings:
            item = ListBookings
            item.payment_id = booking['payment_id']
            item.payment_type = booking['payment_type']
            item.name = booking['name']
            item.room_id = booking['room_id']
            item.customer_id = booking['customer_id']
            item.room_type = booking['room_type']
            item.booking_reference = booking['booking_reference']
            item.check_in = booking['check_in']
            item.check_out = booking['check_out']
        return results

    def get_booking_details_by_payment_type(self, payment_type: str) -> CreateBooking:
        item = CreateBooking()
        booking = Booking.objects.get(payment_type=payment_type)
        item.customer_id = booking.customer_id
        item.payment_id = booking.payment_id
        item.booking_reference = booking.booking_reference
        item.payment_status = booking.payment_status
        item.check_out = booking.check_out
        item.check_in = booking.check_in
        item.room_type = booking.room_type
        item.room_id = booking.room_id
        item.number_of_rooms = booking.number_of_rooms
        return item

    def get_booking_by_booking_id(self, booking_id: int) -> CreateBooking:
        item = CreateBooking()
        booking = Booking.objects.get(booking_id=booking_id)
        item.customer_id = booking.customer_id
        item.payment_id = booking.payment_id
        item.booking_reference = booking.booking_reference
        item.booking_amount = booking.booking_amount
        item.payment_status = booking.payment_status
        item.check_out = booking.check_out
        item.check_in = booking.check_in
        item.room_type = booking.room_type
        item.room_id = booking.room_id
        item.number_of_rooms = booking.number_of_rooms
        return item
