from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.utils import timezone


# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/image')
    file = models.FileField(upload_to='upload/file')
    date = jmodels.jDateTimeField(auto_now_add=True)
    ORGAN_CHOICE = (
        ('enteshar', 'Enteshar'),
        ('fanni', 'Fanni'),
        ('bargozari', 'Bargozari'),
    )
    organ = models.CharField(max_length=100, choices=ORGAN_CHOICE)
    description = models.TextField(blank=True)
    request_user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title