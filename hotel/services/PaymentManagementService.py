from abc import abstractmethod, ABCMeta
from typing import List
from hotel.repository.PaymentRepository import PaymentRepository
from hotel.dto.PaymentDto import *


class PaymentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self, model: CreatePayment):
        raise NotImplementedError

    @abstractmethod
    def make_payment(self, model: DepositPayment):
        raise NotImplementedError

    @abstractmethod
    def change_payment_status(self, model: ChangePaymentStatus):
        raise NotImplementedError


class DefaultPaymentManagementService(PaymentManagementService):
    repository: PaymentRepository

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def create_payment(self, model: CreatePayment):
        self.repository.create_payment(model)

    def make_payment(self, model: DepositPayment):
        self.repository.make_payment(model)

    def change_payment_status(self, model: ChangePaymentStatus):
        self.repository.change_payment_status(model)
