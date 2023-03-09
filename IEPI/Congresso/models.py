from django.db import models
from django.conf import settings

# Create your models here.

class Users(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    email = models.CharField(max_length=256)


