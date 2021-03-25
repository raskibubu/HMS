from datetime import date


class RegisterCustomer:
    customer_id: int
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    confirm_password: str
    address: str
    phone_number: str
    date_of_birth: date


class CustomerDetails:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    address: str
    phone_number: str
    date_of_birth: date


class ListCustomers:
    id: int
    first_name: str
    last_name: str
    address: str
    phone_number: str
    date_of_birth: date


class CustomerID:
    id: int


class CustomerFirstName:
    first_name: str
