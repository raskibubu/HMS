from datetime import date


class RegisterManager:
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


class ManagerDetails:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    address: str
    phone_number: str
    date_of_birth: date


class ListManagers:
    id: int
    first_name: str
    last_name: str
    address: str
    phone_number: str
    date_of_birth: date
