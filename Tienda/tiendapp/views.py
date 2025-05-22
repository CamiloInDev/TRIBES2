from django.shortcuts import render
from productos.models import Categoria, Producto


def home(request):
    return render(request, 'tiendapp/home.html')  

# Vista para listar todas las categorías

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tiendapp/categorias.html', {'categorias': categorias})

# Vista para mostrar productos de una categoría específica

def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'tiendapp/productos_categoria.html', {'categoria': categoria, 'productos': productos})

def colecciones(request):
    categorias = Categoria.objects.all()
    categoria_seleccionada = request.GET.get('categoria')
    
    if categoria_seleccionada:
        productos = Producto.objects.filter(categoria_id=categoria_seleccionada)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'tiendapp/colecciones.html', {
        'categorias': categorias,
        'productos': productos,
        'categoria_actual': int(categoria_seleccionada) if categoria_seleccionada else None
    })



"""
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'tiendapp/home.html'

class ColeccionesView(TemplateView):
    template_name = 'tiendapp/colecciones.html'

"""
