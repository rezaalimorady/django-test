from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodel
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=100)
    send_to = models.ManyToManyField(User)
    description = models.TextField()
    attach_file = models.FileField(upload_to='Messages/attachfile', blank=True)
    date = jmodel.jDateField(default=timezone.now())
    update = jmodel.jDateField(auto_now=True)
    author = models.CharField(max_length=200)



    def __str__(self):
        return self.title
