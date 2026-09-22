from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle'),
]