from django.shortcuts import render
from .models import Producto


def inicio(request):
    productos_activos = Producto.objects.filter(activo=True)
    contexto = {
        'cantidad_productos': productos_activos.count(),
        'productos_recientes': productos_activos.order_by('-creado_en')[:3],
    }
    return render(request, 'productos/inicio.html', contexto)
