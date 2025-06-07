from django.contrib import admin
from .models import Carrito, ItemCarrito

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'creado', 'actualizado')
    list_filter = ('creado', 'actualizado')
    search_fields = ('usuario__username',)
    date_hierarchy = 'creado'  # Agrega una jerarquía de fechas para mejor navegación
    readonly_fields = ('creado', 'actualizado')  # Hacemos estos campos de solo lectura

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad', 'precio')
    list_filter = ('carrito', 'producto')
    search_fields = ('carrito__usuario__username', 'producto__nombre')
