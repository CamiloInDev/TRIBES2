from django.conf import settings
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    
    def __str__(self):
        return self.usuario.username

