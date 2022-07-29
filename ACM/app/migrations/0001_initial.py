# Generated by Django 3.0.8 on 2021-11-16 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventTitle', models.TextField(default='Nothing')),
                ('eventspeakers', models.TextField(default='N/A')),
                ('eventDescription', models.TextField(default='Nothing')),
                ('eventImage', models.ImageField(default='app/images/blog-post-2.jpg', upload_to='eventImg')),
                ('eventdnt', models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 42, 24, 271693, tzinfo=utc))),
                ('eventDate', models.TextField(default='1-1-1970 - 1')),
                ('eventDuration', models.TextField(default='1pm - 2pm')),
                ('eventid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(choices=[('Chair Person', 'Chair Person'), ('Leader', 'Leader'), ('Member', 'Member')], max_length=200)),
                ('typeofmember', models.CharField(choices=[('Core Team', 'Core Team'), ('Web Team', 'Web Team'), ('Social Team', 'Social Team'), ('Management Team', 'Management Team')], max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('linkedlink', models.CharField(max_length=200)),
                ('instalink', models.CharField(max_length=200)),
                ('githublink', models.CharField(max_length=200)),
                ('member_image', models.ImageField(default='app/images/team-1-1.jpg', upload_to='teamMemberImg')),
            ],
        ),
    ]