# Generated by Django 2.0.13 on 2020-07-03 18:56

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200703_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='register',
            field=django_jalali.db.models.jDateField(verbose_name=datetime.datetime(2020, 7, 3, 18, 56, 51, 94180, tzinfo=utc)),
        ),
    ]
