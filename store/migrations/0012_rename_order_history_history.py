# Generated by Django 3.2.12 on 2022-04-20 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_history'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_history',
            new_name='History',
        ),
    ]