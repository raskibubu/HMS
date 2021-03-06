# Generated by Django 3.1.7 on 2021-03-22 16:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_reference', models.IntegerField(max_length=10000)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('number_of_rooms', models.IntegerField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
                ('date_created', models.DateField(default=datetime.date(2021, 3, 22))),
                ('date_updated', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(max_length=10000)),
                ('room_number', models.IntegerField(max_length=10000)),
                ('room_type', models.CharField(max_length=20)),
                ('room_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=20)),
                ('amount', models.IntegerField(max_length=10000000)),
                ('balance', models.IntegerField(max_length=10000000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hotel.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
                ('date_created', models.DateField(default=datetime.date(2021, 3, 22))),
                ('date_updated', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
    ]
