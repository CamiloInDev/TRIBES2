"""Configuración de la aplicación de productos.

Este módulo contiene la configuración específica para la aplicación de productos,
incluyendo la configuración de campos automáticos y el nombre de la aplicación.
"""

from django.apps import AppConfig


class ProductosConfig(AppConfig):
    """Configuración para la aplicación de productos.

    Define la configuración específica para la aplicación de productos,
    incluyendo el tipo de campo automático predeterminado y el nombre de la aplicación.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "productos"
