# Generated by Django 2.0.13 on 2020-07-04 14:05

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20200704_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='register',
            field=django_jalali.db.models.jDateField(verbose_name=datetime.datetime(2020, 7, 4, 14, 5, 44, 578175, tzinfo=utc)),
        ),
    ]
