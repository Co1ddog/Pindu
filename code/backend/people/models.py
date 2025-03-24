from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    balance = models.FloatField(default=0)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(max_length=2, blank=True)


class UserAddress(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    receiver_name = models.CharField(max_length=20, blank=True)
    receiver_phone = models.CharField(max_length=20, blank=True)
    receiver_region = models.CharField(max_length=20, blank=True)
    receiver_place = models.CharField(max_length=20, blank=True)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=300)
    level = models.IntegerField(default=0)
    gender = models.CharField(max_length=2, blank=True)
    birth = models.CharField(max_length=10, blank=True)
    intro = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=11, blank=True)

