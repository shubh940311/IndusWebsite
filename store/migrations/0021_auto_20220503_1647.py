# Generated by Django 3.2.12 on 2022-05-03 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20220503_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='previous',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 47, 48, 109541)),
        ),
        migrations.AlterField(
            model_name='previous',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 47, 48, 110541)),
        ),
    ]
