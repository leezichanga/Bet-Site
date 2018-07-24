from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Deposit(models.Model):
    """docstring for Deposit."""
    mobile_number = models.CharField(max_length=30)
    user_id = models.CharField(max_length=60)
    amount = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Placebet(models.Model):
    game_id = models.CharField(max_length=60)
    amount = models.CharField(max_length=20)
    BOOL_CHOICES = ((True, '0'), (False, '1'), (True, 'x'))
    prediction = models.NullBooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return self.name
