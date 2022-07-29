# Generated by Django 3.2.9 on 2021-11-17 07:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('ppic', models.ImageField(upload_to='pics')),
                ('ptype', models.CharField(choices=[('Event_One', 'Event_One'), ('Event_Two', 'Event_Two'), ('Event_Three', 'Event_Three')], default='other', max_length=50)),
                ('pdesc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='eventdnt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 7, 4, 44, 9477, tzinfo=utc)),
        ),
    ]
