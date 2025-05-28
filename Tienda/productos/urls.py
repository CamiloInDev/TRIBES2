"""URLs para la gestión de productos.

Este módulo define las rutas URL para las vistas relacionadas con productos,
incluyendo listado, detalle y filtrado por categoría.
"""

from django.urls import path

from . import views

#: Patrones de URL para la gestión de productos
urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("<int:producto_id>/", views.detalle_producto, name="detalle_producto"),
    path(
        "categoria/<int:categoria_id>/",
        views.productos_por_categoria,
        name="productos_por_categoria",
    ),
]
