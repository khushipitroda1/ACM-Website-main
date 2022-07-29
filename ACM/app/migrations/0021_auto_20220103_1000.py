# Generated by Django 3.2.5 on 2022-01-03 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20220103_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.PositiveIntegerField()),
                ('sem', models.PositiveIntegerField()),
                ('dept', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='achievements',
            name='datent',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 3, 4, 30, 33, 984135, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='eventdnt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 3, 4, 30, 33, 982134, tzinfo=utc)),
        ),
    ]