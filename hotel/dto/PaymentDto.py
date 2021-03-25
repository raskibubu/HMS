class CreatePayment:
    booking_id: int
    payment_status: str
    amount: float
    balance: float


class ChangePaymentStatus:
    booking_id: int
    payment_status: str


class DepositPayment:
    booking_id: int
    amount: float
    balance: float

