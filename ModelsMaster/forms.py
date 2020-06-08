from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Ambito, TipoObjetivo, Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo
from django.contrib.auth.models import User, Permission

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['Nombre', 'Descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['Nombre'] 

""" class EstructuraForm(ModelForm):
    class Meta:
        model = Estructura
        fields = ['Nombre' ]

class RiesgoForm(ModelForm):
    class Meta:
        model = Riesgo
        fields = ['Nombre']

class TipoIntervinienteForm(ModelForm):
    class Meta:
        model = TipoInterviniente
        fields = ['Nombre'] """

class SectorForm(ModelForm):
    class Meta:
        model = Sector
        fields = ['Nombre', 'Descripcion'] 

class NivelAreaGeograficaForm(ModelForm):
    class Meta:
        model = NivelAreaGeografica
        fields = ['Nivel', 'Nombre', 'Descripcion']

class AreaGeograficaForm(ModelForm):
    class Meta:
        model = AreaGeografica
        fields = ['IdNag','IdParent','Nombre','Descripcion']

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['IdSc','IdAg','Nombre', 'Descripcion'] 

class ModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['IdEmp','Nombre','Descripcion']
        
class BenchmarkingForm(ModelForm):
    class Meta:
        model = Benchmarking
        fields = ['IdSc','IdAg','Nombre','Descripcion','Ciclo','Anyo','Valor']

class PuntosCapituloForm(ModelForm):
    class Meta:
        model = PuntosCapitulo
        fields = ['IdMd','IdAm','Nombre']

class ObjetivoForm(ModelForm):
    class Meta:
        model = Objetivo
        fields = ['IdTo','IdPc','IdParent','Nombre','Descripcion','Codificacion','Anyo']

""" class ObjetivoRelacionadoForm(ModelForm):
    class Meta:
        model = ObjetivoRelacionado
        fields = ['id_or_ob','id_or_ob_asociado','str_or_nombre'] """

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

""" class PermissionForm(ModelForm):
    def init(self, args, **kwargs):
        super(PermissionForm, self).init(args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Permission
        fields = '__all__' """