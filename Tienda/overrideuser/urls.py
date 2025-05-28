"""URLs para la gestión de usuarios personalizados.

Este módulo define las rutas URL para las vistas de autenticación
y gestión de perfiles de usuario personalizados.
"""

from django.urls import path

from . import views

#: Patrones de URL para la gestión de usuarios
urlpatterns = [
    path("registro/", views.registro_view, name="registro"),
    path("inicio-sesion/", views.inicio_sesion_view, name="inicio_sesion"),
    path("cerrar-sesion/", views.cerrar_sesion_view, name="cerrar_sesion"),
    path("editar-perfil/", views.editar_perfil_view, name="editar_perfil"),
    path("eliminar-cuenta/", views.eliminar_cuenta_view, name="eliminar_cuenta"),
]
