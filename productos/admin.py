from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo', 'creado_en')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
