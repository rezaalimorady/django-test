# Generated by Django 2.0.13 on 2020-07-03 22:17

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20200703_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='register',
            field=django_jalali.db.models.jDateField(verbose_name=datetime.datetime(2020, 7, 3, 22, 17, 5, 406765, tzinfo=utc)),
        ),
    ]
