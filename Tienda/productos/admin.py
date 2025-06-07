from django.contrib import admin
from .models import Categoria, Producto

# Registro simple de los modelos
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
