# Generated by Django 2.0.13 on 2020-07-03 18:51

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='attach_file',
            field=models.FileField(blank=True, upload_to='Messages/attachfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=datetime.datetime(2020, 7, 3, 18, 51, 48, 586116, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='message',
            name='send_to',
        ),
        migrations.AddField(
            model_name='message',
            name='send_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
