from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('colecciones/', views.colecciones, name='colecciones'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
]


