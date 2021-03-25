from abc import abstractmethod, ABCMeta
from typing import List
from hotel.repository.CustomerRepository import CustomerRepository
from hotel.dto.CustomerDto import *


class CustomerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_customer(self, model: RegisterCustomer):
        raise NotImplementedError

    @abstractmethod
    def list_customers(self) -> List[ListCustomers]:
        raise NotImplementedError

    @abstractmethod
    def get_details_by_customer(self, user_id: int) -> CustomerDetails:
        raise NotImplementedError

    @abstractmethod
    def get_customer_id(self, user_id: int) -> CustomerID:
        raise NotImplementedError

    @abstractmethod
    def get_customer_first_name(self, user_id: int) -> str:
        raise NotImplementedError


class DefaultCustomerManagementService(CustomerManagementService):
    repository: CustomerRepository

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create_customer(self, model: RegisterCustomer):
        return self.repository.create_customer(model)

    def list_customers(self) -> List[ListCustomers]:
        return self.repository.list_customers()

    def get_details_by_customer(self, user_id: int) -> CustomerDetails:
        return self.repository.get_details_by_customer(user_id)

    def get_customer_id(self, user_id: int) -> int:
        return self.repository.get_customer_id(user_id)

    def get_customer_first_name(self, user_id: int) -> str:
        return self.repository.get_customer_first_name(user_id)

