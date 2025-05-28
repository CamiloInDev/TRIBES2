"""Configuración de la aplicación overrideuser."""

from django.apps import AppConfig


class OverrideuserConfig(AppConfig):
    """Configuración para la aplicación de usuarios personalizados."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "overrideuser"
