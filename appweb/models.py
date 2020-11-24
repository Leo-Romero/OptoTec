from django.db import models
from django.contrib.auth.models import User
import datetime


class Perfil(models.Model):
    """
    Modelo que agrega datos al usuario
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    f_nac = models.DateField('Fecha de nacimiento', blank=True, null=True, help_text="Fecha de nacimiento: (DD/MM/AAAA)")
    f_alta = models.DateField(auto_now_add=True)
    f_acceso = models.DateTimeField(auto_now=True)    # ultima modificacion
    GE = 'GERENCIA'
    SE = 'SECRETARIA'
    ME = 'MEDICO'
    TE = 'TECNICO'
    VE = 'VENTAS'
    CONDICION_CHOICES = [
        (GE, 'GERENCIA'),
        (SE, 'SECRETARIA'),
        (ME, 'MEDICO'),
        (TE, 'TECNICO'),
        (VE, 'VENTAS'),
    ]
    puesto = models.CharField('Puesto', max_length=10, choices=CONDICION_CHOICES, default=VE)
    telefono = models.CharField('Teléfono', max_length=12, blank=True, null=True, help_text="Teléfono particular (e.g. 2923-4123456)")
    interno = models.CharField('Interno Tel.', max_length=4, blank=True, null=True, help_text="Número de interno (e.g. 1234)")

    class Meta:
        permissions = (
            ("gerencia", "Es gerente"),
            ("secretaria", "Es secretaria"),
            ("medico", "Es un medico"),
            ("tecnico", "Es un tecnico"),
            ("ventas", "Es un vendedor"),
        )
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['puesto', 'usuario']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.usuario}"


class Cobertura(models.Model):
    """
    Coberturas medicas
    """
    nombre = models.CharField('Nombre', max_length=50, blank=False, null=False, help_text="Nombre")
    descripcion = models.CharField('Descripción', max_length=100, blank=True, null=True, help_text="Descripción")
  
    class Meta:
        verbose_name = 'Cobertura'
        verbose_name_plural = 'Coberturas'
        ordering = ['nombre']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.nombre}"


class Proveedor(models.Model):
    """
    Modelo de proveedores
    """
    nombre = models.CharField('Nombre', max_length=250, blank=False, null=False)
    cuit = models.CharField('CUIT', max_length=13, blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=250, blank=False, null=False)
    cod_postal = models.CharField('C. Postal', max_length=10, blank=True, null=True)
    ciudad = models.CharField('Ciudad', max_length=50, blank=True, null=True)
    provincia = models.CharField('Provincia', max_length=50, blank=True, null=True)
    pais = models.CharField('País', max_length=50, blank=True, null=True)
    correo = models.EmailField('Email', max_length=254, blank=True, null=True)
    telefono1 = models.CharField('Teléfono', max_length=12, blank=True, null=True)
    telefono2 = models.CharField('Teléfono', max_length=12, blank=True, null=True)
    contacto = models.CharField('Contacto', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.nombre} {self.ciudad}"


class Producto(models.Model):
    """
    Modelo de productos
    """
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=250, blank=False, null=False)
    marca = models.CharField('Marca', max_length=200, blank=True, null=True)
    modelo = models.CharField('Modelo', max_length=200, blank=True, null=True)
    clasificacion = models.CharField('Clasificación', max_length=80, blank=True, null=True)
    lente = models.BooleanField('Lente ?', default=False)
    I = 'IZQUIERDO'
    D = 'DERECHO'
    CONDICION_CHOICES = [
        (I, 'IZQUIERDO'),
        (D, 'DERECHO'),
    ]
    lado = models.CharField('Ojo', max_length=9, choices=CONDICION_CHOICES, default=I, blank=True, null=True)
    L = 'LEJOS'
    C = 'CERCA'
    CONDICION_CHOICES = [
        (L, 'LEJOS'),
        (C, 'CERCA'),
    ]
    distancia = models.CharField('Distancia', max_length=5, choices=CONDICION_CHOICES, default=L, blank=True, null=True)
    armazon = models.BooleanField('Armazón', default=False)
    otros = models.TextField('Otros', blank=True, null=True)
    stock = models.PositiveSmallIntegerField('Stock')
    precio = models.DecimalField('Precio unitario', max_digits=7, decimal_places=2)
   
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if self.lente == False:
            self.distancia = None
            self.lado = None
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.nombre}"


class Paciente(models.Model):
    """
    Modelo de Pacientes
    """
    dni = models.CharField('DNI', max_length=8, blank=False, null=False, help_text="Número de DNI")
    apellido = models.CharField('Apellido', max_length=50, blank=True, null=True, help_text="Apellido")
    nombres = models.CharField('Nombres', max_length=250, blank=True, null=True, help_text="Nombres")
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)
    num_cobertura = models.CharField('Afiliado', max_length=25, blank=False, null=False, help_text="Número de afiliado")
    f_nac = models.DateField('Fecha de nacimiento', blank=True, null=True, help_text="Fecha de nacimiento: (DD/MM/AAAA)")
    M = 'MASCULINO'
    F = 'FEMENINO'
    CONDICION_CHOICES = [
        (M, 'MASCULINO'),
        (F, 'FEMENINO'),
    ]
    sexo  = models.CharField('Sexo', max_length=10, choices=CONDICION_CHOICES, default=M)
    direccion = models.CharField('Dirección', max_length=60, blank=True, null=True, help_text="(e.g. Chiclana 555)")
    ciudad = models.CharField('Ciudad', max_length=50, blank=True, null=True, help_text="(e.g. Bahia Blanca)")
    telefono = models.CharField('Teléfono', max_length=12, blank=True, null=True, help_text="(e.g. 2923-4123456)")
    correo = models.EmailField('Email', max_length=254, blank=True, null=True)
    ocupacion = models.CharField('Ocupación', max_length=120, blank=True, null=True)
    S = 'SOLTERO/A'
    C = 'CASADO/A'
    D = 'DIVORCIADO/A'
    V = 'VIUDO/A'
    CONDICION_CHOICES = [
        (S, 'SOLTERO/A'),
        (C, 'CASADO/A'),
        (D, 'DIVORCIADO/A'),
        (V, 'VIUDO/A'),
    ]
    estadciv = models.CharField('Estado civil', max_length=12, choices=CONDICION_CHOICES, default=S)
    medico = models.ForeignKey(Perfil, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['dni']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.dni} - {self.apellido} {self.nombres}"


class Pedido(models.Model):
    """
    Modelo de pedidos
    """
    fecha = models.DateField('Fecha', default=datetime.date.today, blank=False, null=False, help_text="Fecha: (DD/MM/AAAA)")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    P = 'PENDIENTE'
    D = 'PEDIDO'
    T = 'TALLER'
    F = 'FINALIZADO'
    CONDICION_CHOICES = [
        (P, 'PENDIENTE'),
        (D, 'PEDIDO'),
        (T, 'TALLER'),
        (F, 'FINALIZADO'),
    ]
    estado = models.CharField('Estado', max_length=10, choices=CONDICION_CHOICES, default=P)
    C = 'TARJ CREDITO'
    D = 'TARJ DEBITO'
    V = 'BILL. VIRTUAL'
    E = 'EFECTIVO'
    CONDICION_CHOICES = [
        (C, 'TARJ CREDITO'),
        (D, 'TARJ DEBITO'),
        (V, 'BILL. VIRTUAL'),
        (E, 'EFECTIVO'),
    ]
    subtotal = models.DecimalField('Venta Total $', max_digits=7, decimal_places=2)
    tipo_pago = models.CharField('Tipo de pago', max_length=13, choices=CONDICION_CHOICES, default=E)
    nota = models.TextField('Notas', blank=True, null=True)
    #vendedor = models.CharField('vendedor', max_length=150)
    vendedor = models.ForeignKey(Perfil, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']

    #def get_subtotal(self):
    #    return self.cantidad * self.precio

    def verSubTotal(self):
        return f"{self.subtotal}"
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.fecha} {self.paciente}"


class RenglonPedido(models.Model):
    """
    Modelo de renglones del pedido
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)
    cantidad = models.PositiveSmallIntegerField('Cantidad', default=1)
    total = models.DecimalField('Total', max_digits=7, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.producto.precio * self.cantidad
        """
        producto = Producto.objects.get(id=self.producto.id)
        pedido = Pedido.objects.get(id=self.pedido.id)
        # En caso de actualziar el detalle
        detalle = RenglonPedido.objects.filter(id=self.id)
        if detalle:
            # Más productos
            if self.cantidad > detalle[0].cantidad:
                # Total
                pedido.subtotal += self.total - detalle[0].total
                # Stock
                producto.stock  -= detalle[0].cantidad - self.cantidad
            # Menos productos
            else:
                # Total
                pedido.subtotal -= detalle[0].total - self.total
                # Stock
                producto.stock  += self.cantidad - detalle[0].cantidad
        else:
           # Actualizo el precio
            if pedido.subtotal:
                pedido.subtotal += self.total
            else:
                pedido.subtotal = self.total
            # Actualizo el stock
            producto.stock -= self.cantidad
        producto.save()
        pedido.save()
        """
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Actualizo el precio
        pedido = Pedido.objects.get(id=self.pedido.id)
        pedido.subtotal -= self.total
        pedido.save()
        """
        # Actualizaco el stock
        producto = Producto.objects.get(id=self.producto.id)
        producto.stock += self.cantidad
        producto.save()
        """
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Renglón del pedido'
        verbose_name_plural = 'Renglones de los pedidos'

    def obtenerCantidad(self):
        return f"{self.cantidad} {'unidades' if self.cantidad > 1 else 'unidad'}"

    def __str__(self):
        return self.producto.nombre


class Historia(models.Model):
    """
    Modelo de las historias clinicas
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField('Fecha', default=datetime.date.today, blank=True, null=True, help_text="Fecha: (DD/MM/AAAA)")
    motivo = models.TextField('Motivo de la consulta', blank=True, null=True)
    enf_actual = models.TextField('Enfermedad Actual', blank=True, null=True)
    tratamiento = models.TextField('Tratamiento', blank=True, null=True)
    antecedentes = models.TextField('Antecedentes', blank=True, null=True)

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'
        ordering = ['-fecha']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.fecha}"


class Turno(models.Model):
    """
    Modelo de turnos
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField('Fecha', blank=False, null=False, help_text="Fecha: (DD/MM/AAAA)")
    hora = models.TimeField('Hora', blank=False, null=False, help_text="Hora: (HH/MM)")
    medico = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    concurrio = models.BooleanField('Concurrió', default=False)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['-fecha', 'hora']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.fecha} / {self.hora} : {self.paciente}"
