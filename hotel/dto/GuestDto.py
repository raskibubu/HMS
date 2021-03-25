class CreateGuest:
    booking_id: int
    guest_name: str
    guest_status: str
    room_number: int


class ChangeGuestStatus:
    room_number: int
    guest_status: int


class GuestDetails:
    booking_id: int
    guest_name: str
    guest_status: str
    room_number: int


class ListGuests:
    booking_id: int
    guest_name: str
    guest_status: str
    room_number: int
