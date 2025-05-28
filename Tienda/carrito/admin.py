"""Configuración de la administración para el carrito de compras."""
from typing import ClassVar

from django.contrib import admin

from .models import Carrito, ItemCarrito


class ItemCarritoInline(admin.TabularInline):
    """Configuración inline para los ítems del carrito en el admin."""

    model: ClassVar[ItemCarrito] = ItemCarrito
    extra: ClassVar[int] = 0

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    """Configuración del modelo Carrito en el admin."""

    list_display: ClassVar[tuple[str, ...]] = (
        "usuario", "creado", "actualizado", "total",
    )
    inlines: ClassVar[list] = [ItemCarritoInline]

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    """Configuración del modelo ItemCarrito en el admin."""

    list_display: ClassVar[tuple[str, ...]] = (
        "carrito", "producto", "cantidad", "precio", "subtotal",
    )
