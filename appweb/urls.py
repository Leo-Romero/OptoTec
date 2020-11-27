from django.urls import path
from .views import home, signup, addPerfil, listPerfil, editPerfil, addPaciente, listPaciente, editPaciente, listPacienteMed, addHistoria, listHistoria, addTurno, editTurno, listTurno, delTurno, listPacxFecha, addPedido, listPedido, editPedido, listPedidoT, editPedidoT, addProducto, listProducto, editProducto, listPacienteGer, listPedidoGer, listProdGer, listVentGer
from .views import listRenPedido, addRenPedido, delPedido, vistalistRenPedido


app_name = 'appweb'
urlpatterns = [
    path('', home, name='index'),
    path('signup/', signup, name='signup'),
    path('addPer/', addPerfil, name='addPer'),
    path('listPer/', listPerfil, name='listPer'),
    path('editPer/<int:pk>/', editPerfil, name='editPer'),
    path('addPac/', addPaciente, name='addPac'),
    path('listPac/', listPaciente, name='listPac'),
    path('editPac/<int:pk>/', editPaciente, name='editPac'),
    path('addHis/', addHistoria, name='addHis'),
    path('listHis/<int:pk>/', listHistoria, name='listHis'),
    path('addTur/', addTurno, name='addTur'),
    path('listTur/', listTurno, name='listTur'),
    path('editTur/<int:pk>/', editTurno, name='editTur'),
    path('delTur/<int:pk>/', delTurno, name='delTur'),
    path('listPacxFecha/', listPacxFecha, name='listPacxFecha'),
    path('addPed/', addPedido, name='addPed'),
    path('listPed/', listPedido, name='listPed'),
    path('editPed/<int:pk>/', editPedido, name='editPed'),
    path('delPed/<int:pk>/', delPedido, name='delPed'),

    path('addRenPed/', addRenPedido, name='addRenPed'),
    path('listRenPed/', listRenPedido, name='listRenPed'),
    path('verPed/<int:pk>/', vistalistRenPedido, name='verPed'),
    #path('listRenPedEd/<int:pk>/', listRenPedidoEd, name='listRenPedEd'),
    #path('editRenPed/<int:pk>/', editRenPedido, name='editRenPed'),

    path('listPedT/', listPedidoT, name='listPedT'),
    path('editPedT/<int:pk>/', editPedidoT, name='editPedT'),
    path('addProd/', addProducto, name='addProd'),
    path('listProd/', listProducto, name='listProd'),
    path('editProd/<int:pk>/', editProducto, name='editProd'),
    path('listPacMed/', listPacienteMed, name='listPacMed'),
    path('listPacGer/', listPacienteGer, name='listPacGer'),
    path('listPedGer/', listPedidoGer, name='listPedGer'),
    path('listProdGer/', listProdGer, name='listProdGer'),
    path('listVentGer/', listVentGer, name='listVentGer'),
]
