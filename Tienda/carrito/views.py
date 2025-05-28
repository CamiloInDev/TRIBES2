"""Vistas para la gestión del carrito de compras."""


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from productos.models import Producto

from .models import Carrito, ItemCarrito


@login_required
def ver_carrito(request: HttpRequest) -> HttpResponse:
    """Muestra el contenido del carrito del usuario actual.

    Args:
        request: La petición HTTP

    Returns:
        HttpResponse: Renderiza la plantilla del carrito con los items

    """
    carrito: Carrito
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, "carrito/ver_carrito.html", {"carrito": carrito})

@login_required
def agregar_al_carrito(
    request: HttpRequest,
    producto_id: int,
) -> JsonResponse | HttpResponse:
    """Añade un producto al carrito o incrementa su cantidad si ya existe.

    Args:
        request: La petición HTTP
        producto_id: ID del producto a añadir

    Returns:
        JsonResponse si es AJAX, redirección HTTP en otro caso

    """
    producto: Producto = get_object_or_404(Producto, id=producto_id)
    carrito: Carrito
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    # Verificar si el producto ya está en el carrito
    try:
        item: ItemCarrito = ItemCarrito.objects.get(
            carrito=carrito,
            producto=producto,
        )
        item.cantidad += 1
        item.save()
        messages.success(
            request,
            f"Se incrementó la cantidad de {producto.nombre} en tu carrito.",
        )
    except ItemCarrito.DoesNotExist:
        # Crear nuevo item en el carrito
        ItemCarrito.objects.create(
            carrito=carrito,
            producto=producto,
            precio=producto.precio,
            descripcion=producto.descripcion,
        )
        messages.success(request, f"{producto.nombre} agregado a tu carrito.")

    # Si es una solicitud AJAX, devolver JSON
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse(
            {
                "success": True,
                "total_items": carrito.items.count(),
                "message": f"{producto.nombre} agregado a tu carrito.",
            },
        )

    # Redirigir a la página anterior o al carrito

    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    return redirect("carrito:ver_carrito")

@login_required
def actualizar_cantidad(
    request: HttpRequest,
    item_id: int,
) -> JsonResponse:
    """Actualiza la cantidad de un ítem en el carrito.

    Args:
        request: La petición HTTP
        item_id: ID del ítem a actualizar

    Returns:
        JsonResponse con la nueva cantidad y subtotal, o error

    """
    item: ItemCarrito = get_object_or_404(
        ItemCarrito, id=item_id, carrito__usuario=request.user,
    )

    if request.method == "POST":
        accion: str | None = request.POST.get("accion")
        if accion == "incrementar":
            item.cantidad += 1
        elif accion == "decrementar" and item.cantidad > 1:
            item.cantidad -= 1
        item.save()
        # Si la petición es AJAX, también devuelve el total actualizado
        carrito = item.carrito
        total = float(carrito.total)
        return JsonResponse(
            {
                "cantidad": item.cantidad,
                "subtotal": float(item.subtotal),
                "total": total,
            },
        )
    return JsonResponse({"error": "Método no permitido"}, status=405)

@login_required
def eliminar_del_carrito(
    request: HttpRequest,
    item_id: int,
) -> HttpResponse:
    """Elimina un ítem del carrito.

    Args:
        request: La petición HTTP
        item_id: ID del ítem a eliminar

    Returns:
        Redirección a la vista del carrito

    """
    item: ItemCarrito = get_object_or_404(
        ItemCarrito, id=item_id, carrito__usuario=request.user,
    )
    producto_nombre: str = item.producto.nombre
    item.delete()
    messages.success(request, f"{producto_nombre} eliminado del carrito.")
    return redirect("carrito:ver_carrito")

@login_required
def vaciar_carrito(request: HttpRequest) -> HttpResponse:
    """Vacía completamente el carrito del usuario.

    Args:
        request: La petición HTTP

    Returns:
        Redirección a la vista del carrito

    """
    if request.method == "POST":
        carrito: Carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito.items.all().delete()
        messages.success(request, "El carrito ha sido vaciado.")
    return redirect("carrito:ver_carrito")
