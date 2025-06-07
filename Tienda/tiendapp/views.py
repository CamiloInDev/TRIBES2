"""Vistas para la aplicación principal de la tienda."""

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext
from productos.models import Categoria, Producto


from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.template import loader
from django.http import HttpResponseNotFound

@requires_csrf_token
def custom_404(request, exception=None, template_name='tiendapp/404.html', **kwargs):
    """Vista personalizada para el error 404."""
    # Ignorar cualquier parámetro adicional que pueda venir de la URL
    # Crear contexto con información útil
    context = {
        'request': request,
        'exception': str(exception) if exception else "",
        'path': request.path,
        'status_code': 404
    }
    
    # Cargar la plantilla manualmente para asegurar que se encuentre
    template = loader.get_template(template_name)
    body = template.render(context, request)
    
    # Devolver la respuesta con el código de estado 404
    return HttpResponseNotFound(body)


def test_404(request):
    """Vista de prueba para el error 404."""
    from django.http import Http404
    if request.GET.get('force'):
        raise Http404("Página de prueba 404")
    return custom_404(request)


def home(request: HttpRequest) -> HttpResponse:
    """Vista de inicio de la tienda."""
    return render(request, "tiendapp/home.html")

# Vista para listar todas las categorías

def categorias(request: HttpRequest) -> HttpResponse:
    """Vista para listar todas las categorías."""
    categorias = Categoria.objects.all()
    return render(request, "tiendapp/categorias.html", {"categorias": categorias})

# Vista para mostrar productos de una categoría específica

def productos_por_categoria(
    request: HttpRequest,
    categoria_id: int,
) -> HttpResponse:
    """Vista para mostrar productos de una categoría específica."""
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(
        request,
        "tiendapp/productos_categoria.html",
        {"categoria": categoria, "productos": productos},
    )

def colecciones(request: HttpRequest) -> HttpResponse:
    """Vista para mostrar colecciones filtradas por categoría."""
    categorias = Categoria.objects.all()
    categoria_seleccionada = request.GET.get("categoria")

    if categoria_seleccionada:
        productos = Producto.objects.filter(categoria_id=categoria_seleccionada)
    else:
        productos = Producto.objects.all()

    return render(request, "tiendapp/colecciones.html", {
        "categorias": categorias,
        "productos": productos,
        "categoria_actual": (
            int(categoria_seleccionada) if categoria_seleccionada else None
        ),
    })



"""
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'tiendapp/home.html'

class ColeccionesView(TemplateView):
    template_name = 'tiendapp/colecciones.html'

"""
