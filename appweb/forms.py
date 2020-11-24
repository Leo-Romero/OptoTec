import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil, Paciente, Cobertura, Historia, Turno, Pedido, RenglonPedido, Producto


class SignUpForm(UserCreationForm):
    """
    Formulario de registro de usuarios
    """
    first_name = forms.CharField(max_length=30, required=True, help_text='Nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Apellido')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un email valido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PerfilForm(forms.ModelForm):
    """
    Formulario de relleno de Perfil
    """
    class Meta:
        model = Perfil
        fields = (
            'usuario',
            'f_nac',
            'puesto',
            'telefono',
            'interno',
        )


class PerfilFormEdit(forms.ModelForm):
    """
    Formulario de edicion para Perfil
    el campo usuario es de solo lectura
    """
    class Meta:
        model = Perfil
        fields = (
            'usuario',
            'f_nac',
            'puesto',
            'telefono',
            'interno',
        )
        labels = {
            'usuario': ('Código de usuario'),
        }
        help_texts = {
            'usuario': ('SOLO LECTURA'),
        }
        widgets = {
            'usuario': forms.TextInput(attrs={'readonly': True}),
        }


class PacienteForm(forms.ModelForm):
    """
    Formulario para Pacientes, campo 'medico' se rellena con solo puesto=medico
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medico'].queryset = Perfil.objects.filter(puesto='MEDICO')
    
    class Meta:
        model = Paciente
        fields = (
            'dni',
            'apellido',
            'nombres',
            'cobertura',
            'num_cobertura',
            'f_nac',
            'sexo',
            'direccion',
            'ciudad',
            'telefono',
            'correo',
            'ocupacion',
            'estadciv',
            'medico',
        )



class HistoriaForm(forms.ModelForm):
    """
    Formulario para historias clinicas
    """
    class Meta:
        model = Historia
        fields = (
            'paciente',
            'fecha',
            'motivo',
            'enf_actual',
            'tratamiento',
            'antecedentes',
        )


class TurnoForm(forms.ModelForm):
    """
    Formulario para turnos, campo 'medico' se rellena con solo puesto=medico
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medico'].queryset = Perfil.objects.filter(puesto='MEDICO')
    
    class Meta:
        model = Turno
        fields = (
            'paciente',
            'fecha',
            'hora',
            'medico',
            'concurrio',
        )
        widgets = {
            'fecha': forms.NumberInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        } 


class FiltroFechas(forms.Form):
    """
    Formulario para ingresar campo desde y hasta
    """
    desde = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}),
    )
    hasta = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}),
    )


class PedidoForm(forms.ModelForm):
    """
    Formulario de Pedidos
    """
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoRengForm(forms.ModelForm):
    """
    Formulario para los renglones del pedido
    """
    class Meta:
        model = RenglonPedido
        fields = '__all__'

class PedidoTForm(forms.ModelForm):
    """
    Para el taller
    """
    class Meta:
        model = Pedido
        fields = (
            'fecha',
       #     'cantidad',
            'nota',
        )
        widgets = {
            'fecha': forms.TextInput(attrs={'readonly': True}),
      #      'cantidad': forms.TextInput(attrs={'readonly': True}),
            'nota': forms.Textarea(attrs={'readonly': True}),
        }
        help_texts = {
            'fecha': ('SOLO LECTURA'),
       #     'cantidad': ('SOLO LECTURA'),
            'nota': ('SOLO LECTURA'),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class FiltroFechasCheck(forms.Form):
    """
    Filtro entre fechas y campo check
    """
    desde = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}),
    )
    hasta = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}),
    )
    concurrieron = forms.TypedChoiceField(
        choices=((False, 'No'), (True, 'Si')),
        widget=forms.RadioSelect
    )
