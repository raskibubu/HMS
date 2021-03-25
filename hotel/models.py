from django.db import models
from django.contrib.auth.models import User
import datetime


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"""{self.user.first_name}\t{self.user.last_name}\t{self.phone_number}"""


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"""{self.user.first_name}\t{self.user.last_name}\t{self.phone_number}"""


class Rooms(models.Model):
    room_id = models.IntegerField()
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20)

    def __str__(self):
        return f"""{self.room_number}\t{self.room_status}\t{self.room_type}"""


class Booking(models.Model):
    payment_id = models.CharField(null=True, max_length=40)
    payment_type = models.CharField(max_length=40, null=True)
    payment_status = models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=20, null=True)
    room_id = models.IntegerField(null=True)
    customer_id = models.IntegerField(null=True)
    room_type = models.CharField(max_length=40, null=True)
    booking_reference = models.CharField(max_length=50, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_rooms = models.IntegerField()
    booking_amount = models.FloatField(null=True)

    def __str__(self):
        return f"""{self.check_in}\t{self.check_out}\t\t{self.number_of_rooms}"""


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    booking = models.ForeignKey(Booking, on_delete=models.RESTRICT, null=True)
    payment_status = models.CharField(max_length=20, null=True)
    payment_type = models.CharField(max_length=40, null=True)
    amount = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return f"""{self.payment_status}\t{self.amount}\t{self.balance}"""


class Guest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, default=None)
    booking = models.ForeignKey(Booking, on_delete=models.RESTRICT)
    booking_reference = models.CharField(max_length=100, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.RESTRICT, default=None)
    status = models.CharField(max_length=20)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"""{self.name}\t{self.status}"""
