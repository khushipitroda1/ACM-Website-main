# Generated by Django 3.0.8 on 2021-11-16 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='eventdnt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 42, 44, 294145, tzinfo=utc)),
        ),
    ]
