from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodel
from django.utils import timezone
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='UserProfile/images')
    register = jmodel.jDateField(timezone.now())

    def __str__(self):
        return self.user.username

