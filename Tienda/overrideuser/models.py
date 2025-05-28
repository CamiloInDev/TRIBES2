"""Modelos para usuarios personalizados.

Este módulo define el modelo de usuario personalizado que extiende el modelo de usuario
predeterminado de Django con campos adicionales para almacenar información de contacto
y perfil del usuario.
"""


from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Usuario personalizado que extiende el modelo de usuario de Django.

    Extiende el modelo AbstractUser para incluir campos adicionales como
    teléfono y dirección. También personaliza el comportamiento por defecto
    del modelo de usuario.
    """

    telefono = models.CharField(
        max_length=20,
        blank=True,
        default="",
        help_text="Número de teléfono de contacto",
    )

    direccion = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Dirección de residencia",
    )

    # Configuración del modelo
    class Meta:
        """Metainformación de la clase CustomUser."""

        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["-date_joined"]




    def __str__(self) -> str:
        """Devuelve el nombre completo del usuario o el username si no hay nombre."""
        nombre = f"{self.first_name} {self.last_name}".strip()
        return nombre or self.username
