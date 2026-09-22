from django.shortcuts import get_object_or_404, render
from .models import Producto


def inicio(request):
    productos_activos = Producto.objects.filter(activo=True)

    contexto = {
        'cantidad_productos': productos_activos.count(),
        'productos_recientes': productos_activos.order_by('-creado_en')[:3],
    }

    return render(request, 'productos/inicio.html', contexto)


def detalle_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id,
        activo=True
    )

    contexto = {
        'producto': producto,
    }

    return render(request, 'productos/detalle.html', contexto)