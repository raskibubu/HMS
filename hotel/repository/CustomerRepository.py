from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from hotel.models import Customer
from hotel.dto.CustomerDto import *


class CustomerRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_customer(self, model: RegisterCustomer) -> int:
        raise NotImplementedError

    @abstractmethod
    def list_customers(self) -> List[ListCustomers]:
        raise NotImplementedError

    @abstractmethod
    def get_details_by_customer(self, user_id: int) -> CustomerDetails:
        raise NotImplementedError

    @abstractmethod
    def get_customer_id(self, user_id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_customer_first_name(self, user_id: int) -> str:
        raise NotImplementedError


class DjangoORMACustomerRepository(CustomerRepository):
    def create_customer(self, model: RegisterCustomer) -> int:
        customer = Customer()
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        customer.user = user
        group = Group.objects.get(name="Customers")
        user.groups.add(group)

        customer.address = model.address
        customer.phone_number = model.phone_number
        customer.date_of_birth = model.date_of_birth
        customer.save()
        customer_id = customer.id
        return customer_id

    def list_customers(self) -> List[ListCustomers]:
        customers = list(
            Customer.objects.values('id', 'user__username', 'user__first_name', 'user__last_name',
                                    'phone_number'))
        results: List[ListCustomers] = []

        for customer in customers:
            item = ListCustomers()
            item.id = customer['id']
            item.phone_number = customer['phone_number']
            item.first_name = customer['user__first_name']
            item.last_name = customer['user__last_name']
            item.username = customer['user__username']
            results.append(item)
        return results

    def get_details_by_customer(self, user_id: int) -> CustomerDetails:
        customer = Customer.objects.values("user_id", "user__first_name", "user__last_name",
                                           "user__username", "user__email", "address", "phone_number",
                                           "date_of_birth").get(
            user_id=user_id)
        item = CustomerDetails()
        try:
            item.id = customer['user_id']
            item.first_name = customer['user__first_name']
            item.last_name = customer['user__last_name']
            item.username = customer['user__username']
            item.email = customer['user__email']
            item.address = customer['address']
            item.phone_number = customer['phone_number']
            item.date_of_birth = customer['date_of_birth']
            return item
        except Customer.DoesNotExist as e:
            raise e

    def get_customer_id(self, user_id: int) -> int:
        try:

            customer = Customer.objects.values('user_id').get(user_id=user_id)
            item = CustomerID()
            item.id = customer['user_id']
            return int(item.id)
        except Customer.DoesNotExist as e:
            raise e

    def get_customer_first_name(self, user_id: int) -> str:
        try:
            customer = Customer.objects.values('user__first_name').get(user_id=user_id)
            item = CustomerFirstName()
            item.first_name = customer['user__first_name']
            return str(item.first_name)
        except Customer.DoesNotExist as e:
            raise e
