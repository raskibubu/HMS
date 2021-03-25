from abc import abstractmethod, ABCMeta
from hotel.models import Payment
from hotel.dto.PaymentDto import *


class PaymentRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self, model: CreatePayment):
        raise NotImplementedError

    @abstractmethod
    def make_payment(self, model: DepositPayment):
        raise NotImplementedError

    @abstractmethod
    def change_payment_status(self, model: ChangePaymentStatus):
        raise NotImplementedError


class DjangoORMAPaymentRepository(PaymentRepository):
    def create_payment(self, model: CreatePayment):
        payment = Payment()
        payment.payment_status = model.payment_status
        payment.booking.payment_status = model.payment_status
        payment.booking.booking_reference = model.booking_id
        payment.balance = model.balance
        payment.amount = model.amount
        payment.save()

    def make_payment(self, model: DepositPayment):
        payment = Payment.objects.get(customer__payment__booking_id=model.booking_id)
        payment.balance = model.balance
        payment.save()

    def change_payment_status(self, model: ChangePaymentStatus):
        payment = Payment.objects.get(customer__payment__booking_id=model.booking_id)
        payment.payment_status = model.payment_status
        payment.save()
