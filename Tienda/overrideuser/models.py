from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
