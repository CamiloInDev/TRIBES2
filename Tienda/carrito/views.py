from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from productos.models import Producto

from .models import Carrito, ItemCarrito


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    
    # Verificar si el producto ya está en el carrito
    try:
        item = ItemCarrito.objects.get(carrito=carrito, producto=producto)
        item.cantidad += 1
        item.save()
        messages.success(request, f'Se incrementó la cantidad de {producto.nombre} en tu carrito.')
    except ItemCarrito.DoesNotExist:
        # Crear nuevo item en el carrito
        ItemCarrito.objects.create(
            carrito=carrito,
            producto=producto,
            precio=producto.precio,
            descripcion=producto.descripcion
        )
        messages.success(request, f'{producto.nombre} agregado a tu carrito.')
    
    # Si es una solicitud AJAX, devolver JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'total_items': carrito.items.count(),
            'message': f'{producto.nombre} agregado a tu carrito.'
        })
    
    # Redirigir a la página anterior o al carrito
    return redirect(request.META.get('HTTP_REFERER', 'ver_carrito'))

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad > 0:
            item.cantidad = cantidad
            item.save()
            messages.success(request, 'Cantidad actualizada.')
        else:
            item.delete()
            messages.success(request, 'Producto eliminado del carrito.')
    
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    producto_nombre = item.producto.nombre
    item.delete()
    messages.success(request, f'{producto_nombre} eliminado de tu carrito.')
    return redirect('ver_carrito')

@login_required
def vaciar_carrito(request):
    if request.method == 'POST':
        carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito.items.all().delete()
        messages.success(request, 'Tu carrito ha sido vaciado.')
    return redirect('ver_carrito')
