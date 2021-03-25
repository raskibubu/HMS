# Generated by Django 3.1.7 on 2021-03-23 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20210323_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='hotel.customer'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hotel.booking'),
        ),
    ]