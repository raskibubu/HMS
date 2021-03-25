from datetime import date


class CreateBooking:
    room_id: int
    customer_id: int
    payment_type: str
    payment_id: str
    room_type: str
    booking_reference: str
    customer_id: int
    check_in: date
    check_out: date
    number_of_rooms: int
    payment_status: int
    payment_status: str
    booking_amount: float


class ListBookings:
    payment_type: int
    payment_id: str
    booking_reference: int
    customer_id: int
    check_in: date
    check_out: date
    room_number: int
    room_type: str
    customer_id: int
    room_id: int
    name: str


class BookingDetails:
    booking_reference: int
    customer_id: int
    check_in: date
    check_out: date
    room_number: int
    room_type: str
    payment_status: int
    customer_id: int


class BookingID:
    booking_reference: str


class BookedRoomID:
    room_id: int
