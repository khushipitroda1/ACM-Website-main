# Generated by Django 3.2.9 on 2021-11-16 10:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_events_eventdnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='eventdnt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 10, 55, 44, 923617, tzinfo=utc)),
        ),
    ]