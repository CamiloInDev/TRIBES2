"""Configuración de la aplicación principal de la tienda."""

from django.apps import AppConfig


class TiendappConfig(AppConfig):
    """Configuración para la aplicación principal de la tienda."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "tiendapp"
