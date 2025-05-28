"""URLs principales de la tienda.

Este módulo define las rutas URL principales de la aplicación de la tienda,
incluyendo la página de inicio, colecciones y categorías.
"""

from django.urls import path

from . import views

#: Patrones de URL principales de la tienda
urlpatterns = [
    path("", views.home, name="Home"),
    path("colecciones/", views.colecciones, name="colecciones"),
    path("categorias/", views.categorias, name="categorias"),
    path(
        "categorias/<int:categoria_id>/",
        views.productos_por_categoria,
        name="productos_por_categoria",
    ),
]


