from django.contrib import admin
from .models import Perfil, Cobertura, Proveedor, Producto, Pedido, RenglonPedido, Paciente, Historia, Turno

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'puesto', 'interno', 'f_acceso')
    list_filter = ('usuario',)


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Cobertura)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(RenglonPedido)
admin.site.register(Paciente)
admin.site.register(Historia)
admin.site.register(Turno)
