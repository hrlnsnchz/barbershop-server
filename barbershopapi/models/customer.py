from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()