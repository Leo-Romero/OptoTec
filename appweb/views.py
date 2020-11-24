import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType

from .forms import SignUpForm, PerfilForm, PerfilFormEdit, PacienteForm, HistoriaForm, TurnoForm, FiltroFechas, PedidoForm, PedidoRengForm, PedidoTForm, ProductoForm, FiltroFechasCheck
from .models import Perfil, Paciente, Cobertura, Historia, Turno, Pedido, RenglonPedido, Producto

"""
Seteos de permisos
"""
def borraPermisoGerencia(request, user_id):
    """
    Borra permiso
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.gerencia')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='gerencia',
        content_type=content_type,
    )
    user.user_permissions.remove(permission)
    
    # Checking the cached permission set
    user.has_perm('appweb.gerencia')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.gerencia')  # True


def borraPermisoSecretaria(request, user_id):
    """
    Borra permiso
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.secretaria')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='secretaria',
        content_type=content_type,
    )
    user.user_permissions.remove(permission)
    
    # Checking the cached permission set
    user.has_perm('appweb.secretaria')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.secretaria')  # True


def borraPermisoMedico(request, user_id):
    """
    Borra permiso
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.medico')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='medico',
        content_type=content_type,
    )
    user.user_permissions.remove(permission)
    
    # Checking the cached permission set
    user.has_perm('appweb.medico')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.medico')  # True


def borraPermisoTecnico(request, user_id):
    """
    Borra permiso
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.tecnico')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='tecnico',
        content_type=content_type,
    )
    user.user_permissions.remove(permission)
    
    # Checking the cached permission set
    user.has_perm('appweb.tecnico')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.tecnico')  # True


def borraPermisoVentas(request, user_id):
    """
    Borra permiso
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.ventas')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='ventas',
        content_type=content_type,
    )
    user.user_permissions.remove(permission)
    
    # Checking the cached permission set
    user.has_perm('appweb.ventas')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.ventas')  # True


def setPermisoGerencia(request, user_id):
    """
    Setea permiso de gerencia
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.gerencia')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='gerencia',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('appweb.gerencia')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.gerencia')  # True


def setPermisoSecretaria(request, user_id):
    """
    Setea permiso de secretaria
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.secretaria')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='secretaria',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('appweb.secretaria')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.secretaria')  # True


def setPermisoMedico(request, user_id):
    """
    Setea permiso de medico
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.medico')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='medico',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('appweb.medico')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.medico')  # True


def setPermisoTecnico(request, user_id):
    """
    Setea permiso de tecnico
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.tecnico')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='tecnico',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('appweb.tecnico')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.tecnico')  # True


def setPermisoVentas(request, user_id):
    """
    Setea permiso de ventas
    """
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('appweb.ventas')

    content_type = ContentType.objects.get_for_model(Perfil)
    permission = Permission.objects.get(
        codename='ventas',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('appweb.ventas')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('appweb.ventas')  # True


##################################################################


"""
Varios
"""
def home(request):
    """
    index
    """
    # Número de visitas a esta vista, contadas en la variable de sesión
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_visits': num_visits,
    }

    return render(request, "index.html", context=context)


def signup(request):
    """
    Funcion para agregar usuarios desde la web
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'appweb/signup.html', {'form': form})


##################################################################


"""
Perfiles
"""
def existeUsr(request, nombre):
    """
    Existe el perfil del usuario ?
    """
    try:
        usr = Perfil.objects.get(usuario=nombre)
    
    except Perfil.DoesNotExist:
        return False
    else:
        return True


@login_required
@permission_required('appweb.secretaria')
def addPerfil(request):
    """
    Funcion para agregar perfiles y permisos
    """
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            if existeUsr(request, data.usuario):
                messages.error(request, 'Ya existe el perfil', extra_tags='puesto')
                print(form.errors)
            else:
                data.save()
                user = User.objects.get(username=data.usuario)
                if data.puesto == 'GERENCIA':
                    setPermisoGerencia(request, user.id)
                    setPermisoSecretaria(request, user.id)
                    setPermisoMedico(request, user.id)
                    setPermisoTecnico(request, user.id)
                    setPermisoVentas(request, user.id)
                if data.puesto == 'SECRETARIA':
                    setPermisoSecretaria(request, user.id)
                if data.puesto == 'MEDICO':
                    setPermisoMedico(request, user.id)
                if data.puesto == 'TECNICO':
                    setPermisoTecnico(request, user.id)
                if data.puesto == 'VENTAS':
                    setPermisoVentas(request, user.id)
            return redirect('/')
    else:
        form = PerfilForm()
    return render(request, 'appweb/agregoPer.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def editPerfil(request, pk):
    """
    Funcion para editar perfiles y permisos
    """
    data = Perfil.objects.get(id = pk)
    if request.method == 'POST':
        form = PerfilFormEdit(request.POST, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            user = User.objects.get(username=data.usuario)

            # Borro todos los permisos
            borraPermisoGerencia(request, user.id)
            borraPermisoSecretaria(request, user.id)
            borraPermisoMedico(request, user.id)
            borraPermisoTecnico(request, user.id)
            borraPermisoVentas(request, user.id)

            # Agrego el permiso necesario
            if data.puesto == 'GERENCIA':
                setPermisoGerencia(request, user.id)
                setPermisoSecretaria(request, user.id)
                setPermisoMedico(request, user.id)
                setPermisoTecnico(request, user.id)
                setPermisoVentas(request, user.id)
            if data.puesto == 'SECRETARIA':
                setPermisoSecretaria(request, user.id)
            if data.puesto == 'MEDICO':
                setPermisoMedico(request, user.id)
            if data.puesto == 'TECNICO':
                setPermisoTecnico(request, user.id)
            if data.puesto == 'VENTAS':
                setPermisoVentas(request, user.id)
            return redirect('/')
    else:
        form = PerfilFormEdit(instance=data)
    return render(request, 'appweb/editPer.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def listPerfil(request):
    perfiles = Perfil.objects.all()
    return render(request, 'appweb/perfil_list.html', {'perfil_list': perfiles})


##################################################################


"""
Pacientes
"""
@login_required
@permission_required('appweb.secretaria')
def addPaciente(request):
    """
    Funcion para agregar pacientes
    """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/')
    else:
        form = PacienteForm()
    return render(request, 'appweb/agregoPac.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def editPaciente(request, pk):
    """
    Funcion para editar pacientes
    """
    data = Paciente.objects.get(id = pk)
    if request.method == 'GET':
        form = PacienteForm(instance=data)
    else:
        form = PacienteForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        redirect('/')
    return render(request, 'appweb/editPac.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def listPaciente(request):
    """
    Funcion para listar pacientes
    """
    pacientes = Paciente.objects.all()
    return render(request, 'appweb/paciente_list.html', {'paciente_list': pacientes})


@login_required
@permission_required('appweb.medico')
def listPacienteMed(request):
    """
    listado de pacientes para medicos filtrado por username
    """
    username = None
    username = request.user.username
    nombre = User.objects.get(username=username)
    nom = Perfil.objects.get(usuario=nombre)
    pacientes = Paciente.objects.filter(medico = nom)

    return render(request, 'appweb/paciente_listMed.html', {'paciente_list': pacientes})


##################################################################


"""
Historias
"""
@login_required
@permission_required('appweb.medico')
def addHistoria(request):
    """
    Funcion para agregar historias
    """
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/')
    else:
        form = HistoriaForm()
    return render(request, 'appweb/agregoHis.html', {'form': form})


@login_required
@permission_required('appweb.medico')
def listHistoria(request, pk):
    """
    Listado de Historias clinicas de paciente pk
    """
    filtro = None
    historias=Historia.objects.filter(paciente=pk)
    return render(request, 'appweb/historia_list.html', {'historia_list': historias})


##################################################################


"""
Turnos
"""
@login_required
@permission_required('appweb.secretaria')
def addTurno(request):
    """
    Funcion para agregar turnos
    """
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/')

    else:
        form = TurnoForm()
    return render(request, 'appweb/agregoTur.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def editTurno(request, pk):
    """
    Funcion para editar turnos
    """
    data = Turno.objects.get(id = pk)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/')
    else:
        form = TurnoForm(instance=data)
    return render(request, 'appweb/editTur.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def delTurno(request, pk):
    """
    Funcion para eliminar turnos
    """
    data = Turno.objects.get(id = pk)
    if request.method == 'POST':
        data.delete()
        return redirect('appweb:listTur')
    return render(request, 'appweb/delTur.html', {'data':data})


@login_required
@permission_required('appweb.secretaria')
def listTurno(request):
    """
    Funcion para listar turnos
    """
    turnos = Turno.objects.all()
    return render(request, 'appweb/turno_list.html', {'turno_list': turnos})


@login_required
@permission_required('appweb.medico')
def listPacxFecha(request):
    """
    Lista pacientes por fecha y medico
    """
    username = None
    username = request.user.username
    nombre = User.objects.get(username=username)
    nom = Perfil.objects.get(usuario=nombre)

    filtro = None
    if request.method == 'POST':
        form = FiltroFechas(request.POST)
        
        if form.is_valid():
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            filtro=Turno.objects.filter(fecha__range=(desde, hasta), medico=(nom))
    else:
        form = FiltroFechas()
    return render(request, 'appweb/listPacxFecha.html', {'form': form,'turno_list': filtro})


##################################################################


"""
Pedidos
"""
@login_required
@permission_required('appweb.ventas')
def addPedido(request):
    """
    Funcion para agregar ventas
    """
    #username = None
    #username = request.user.username

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.vendedor = username
            data.save()
            return redirect('appweb:listRenPed')
    else:
        form = PedidoForm()
    return render(request, 'appweb/agregoPed.html', {'form': form})


@login_required
@permission_required('appweb.ventas')
def addRenPedido(request):
    """
    Funcion para agregar renglones de pedidos
    """
    #username = None
    #username = request.user.username

    if request.method == 'POST':
        form = PedidoRengForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.vendedor = username
            data.save()
            return redirect('appweb:listRenPed')
    else:
        form = PedidoRengForm()
    return render(request, 'appweb/agregoRenPed.html', {'form': form})


@login_required
@permission_required('appweb.ventas')
def listPedido(request):
    """
    Todos los pedidos menos los FINALIZADO
    """
    pedidos = Pedido.objects.exclude(estado__exact='FINALIZADO')
    return render(request, 'appweb/pedido_list.html', {'pedido_list': pedidos})


@login_required
@permission_required('appweb.ventas')
def listRenPedido(request):
    """
    Todos
    """
    renglones = RenglonPedido.objects.all()
    return render(request, 'appweb/pedido_listR.html', {'renglon_list': renglones})


@login_required
@permission_required('appweb.ventas')
def editPedido(request, pk):
    """
    Editar pedidos
    """
    data = Pedido.objects.get(id = pk)
    if request.method == 'GET':
        form = PedidoForm(instance=data)
    else:
        form = PedidoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        redirect('/')
    return render(request, 'appweb/editPed.html', {'form': form})


##################################################################


"""
Pedidos para el taller
"""
@login_required
@permission_required('appweb.tecnico')
def listPedidoT(request):
    """
    Lista solo los pedidos con estado = TALLER
    """
    pedidos = Pedido.objects.filter(estado__exact='TALLER')
    return render(request, 'appweb/pedido_listT.html', {'pedido_list': pedidos})


@login_required
@permission_required('appweb.tecnico')
def editPedidoT(request, pk):
    """
    Solo cambia el estado a Finalizado
    """
    data = Pedido.objects.get(id = pk)

    if request.method == 'GET':
        form = PedidoTForm(instance=data)
    else:
        form = PedidoTForm(request.POST, instance=data)
        if form.is_valid():
            data.estado = 'FINALIZADO'
            form.save()
            return redirect('appweb:listPedT')
    return render(request, 'appweb/editPedT.html', {'form': form})


##################################################################


"""
Producto
"""
@login_required
@permission_required('appweb.secretaria')
def addProducto(request):
    """
    Funcion para agregar productos
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductoForm()
    return render(request, 'appweb/agregoProd.html', {'form': form})


@login_required
@permission_required('appweb.secretaria')
def listProducto(request):
    """
    Funcion para listar Productos
    """
    productos = Producto.objects.all()
    return render(request, 'appweb/producto_list.html', {'producto_list': productos})


@login_required
@permission_required('appweb.secretaria')
def editProducto(request, pk):
    """
    Funcion para editar productos
    """
    data = Producto.objects.get(id = pk)
    if request.method == 'GET':
        form = ProductoForm(instance=data)
    else:
        form = ProductoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        redirect('/')
    return render(request, 'appweb/editPed.html', {'form': form})


##################################################################


"""
Listados varios gerencia
"""
@login_required
@permission_required('appweb.gerencia')
def listPacienteGer(request):
    """
    Pacientes que asistieron o NO a los turnos en la semana/mes (desde / hasta)
    """
    filtro = None
    if request.method == 'POST':
        form = FiltroFechasCheck(request.POST)
        
        if form.is_valid():
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            fueron = request.POST.get("concurrieron")
            filtro=Turno.objects.filter(fecha__range=(desde, hasta), concurrio=(fueron))
    else:
        form = FiltroFechasCheck()
    return render(request, 'appweb/listPacxFecha.html', {'form': form,'turno_list': filtro})


@login_required
@permission_required('appweb.gerencia')
def listPedidoGer(request):
    """
    Pacientes que hicieron por lo menos un Pedido en la semana/mes (desde / hasta)
    """
    filtro = None
    if request.method == 'POST':
        form = FiltroFechas(request.POST)
        
        if form.is_valid():
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            filtro=Pedido.objects.filter(fecha__range=(desde, hasta))
    else:
        form = FiltroFechas()
    return render(request, 'appweb/listPedGer.html', {'form': form,'pedido_list': filtro})


@login_required
@permission_required('appweb.gerencia')
def listProdGer(request):
    """
    Productos más vendidos en el mes (desde / hasta)
    """
    filtro = None
    if request.method == 'POST':
        form = FiltroFechas(request.POST)
        
        if form.is_valid():
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            filtro=Pedido.objects.filter(fecha__range=(desde, hasta), estado=('FINALIZADO')).order_by('-cantidad')
    else:
        form = FiltroFechas()
    return render(request, 'appweb/listProdGer.html', {'form': form,'pedido_list': filtro})


@login_required
@permission_required('appweb.gerencia')
def listVentGer(request):
    """
    Ventas totales por mes clasificadas por Vendedores
    Listado de ventas filtrado por fechas
    calculo subtotal y luego hago un bucle for del filtro para totalizar
    """
    filtro = None
    subt = 0
    total = 0
    if request.method == 'POST':
        form = FiltroFechas(request.POST)
        
        if form.is_valid():
            desde = request.POST.get("desde")
            hasta = request.POST.get("hasta")
            filtro=Pedido.objects.filter(fecha__range=(desde, hasta), estado=('FINALIZADO')).order_by('vendedor')
            for subtotal in filtro:
                subt = subtotal.cantidad * subtotal.precio
                total = total + subt 
                subt = 0
    else:
        form = FiltroFechas()
    return render(request, 'appweb/listVentas.html', {'form': form,'pedido_list': filtro,'total': total})