from django.contrib import admin
from .models import Categoria, Producto, Cliente, Orden

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Orden)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria','fecha_registro')