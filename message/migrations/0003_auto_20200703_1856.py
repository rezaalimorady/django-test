# Generated by Django 2.0.13 on 2020-07-03 18:56

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20200703_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='update',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2020, 7, 3)),
        ),
    ]
