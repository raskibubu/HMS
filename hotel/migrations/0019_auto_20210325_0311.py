# Generated by Django 3.1.7 on 2021-03-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_auto_20210325_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_id',
            field=models.IntegerField(null=True),
        ),
    ]