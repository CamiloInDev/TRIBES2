"""Vistas para la gestión de productos."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Categoria, Producto


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Vista para listar todos los productos."""
    productos = Producto.objects.all()
    return render(request, "productos/lista_productos.html", {"productos": productos})

def detalle_producto(
    request: HttpRequest,
    producto_id: int,
) -> HttpResponse:
    """Vista para mostrar el detalle de un producto."""
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "productos/detalle_producto.html", {"producto": producto})

def productos_por_categoria(
    request: HttpRequest,
    categoria_id: int,
) -> HttpResponse:
    """Vista para mostrar productos filtrados por categoría."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(
        request,
        "productos/productos_por_categoria.html",
        {
            "categoria": categoria,
            "productos": productos,
        },
    )
