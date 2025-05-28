"""Configuración del panel de administración para la aplicación de productos.

Este módulo registra los modelos de la aplicación de productos en el panel
de administración de Django, permitiendo su gestión a través de la interfaz
administrativa.
"""

from django.contrib import admin

from .models import Categoria, Producto

# Registrar modelos para que sean accesibles desde el panel de administración
admin.site.register(Categoria)
admin.site.register(Producto)
