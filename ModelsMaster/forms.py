from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Ambito, TipoObjetivo, Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo, Estructura, Meta, AccionMeta, IndicadorAccionProceso, SeguimientoIndicadores, DocumentosSistema, Proceso
from django.contrib.auth.models import User, Permission

class AmbitoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AmbitoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Ambito
        fields = ['Nombre', 'Descripcion']

class TipoObjetivoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoObjetivoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = TipoObjetivo
        fields = ['Nombre', 'Descripcion']

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
    def __init__(self, *args, **kwargs):
        super(SectorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Sector
        fields = ['Nombre', 'Descripcion'] 

class NivelAreaGeograficaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NivelAreaGeograficaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = NivelAreaGeografica
        fields = ['Nivel', 'Nombre', 'Descripcion']

class AreaGeograficaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AreaGeograficaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdNag'].queryset = NivelAreaGeografica.objects.filter(Eliminado=False)
        self.fields['IdParent'].queryset = AreaGeografica.objects.filter(Eliminado=False)
    
    class Meta:
        model = AreaGeografica
        fields = ['IdNag','IdParent','Nombre','Descripcion']
        labels = {
            'IdNag':'Nivel Área Geográfica',
            'IdParent':'Area Geográfica Padre'
        }

class EmpresaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdSc'].queryset = Sector.objects.filter(Eliminado=False)
        self.fields['IdAg'].queryset = AreaGeografica.objects.filter(Eliminado=False)
    class Meta:
        model = Empresa
        fields = ['IdSc','IdAg','Nombre', 'Descripcion'] 
        labels = {
            'IdSc':'Sector',
            'IdAg':'Área Geográfica'
        }

class ModeloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModeloForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdEmp'].queryset = Empresa.objects.filter(Eliminado=False)
    class Meta:
        model = Modelo
        fields = ['IdEmp','Nombre','Descripcion']
        labels = {
            'IdEmp':'Empresa'
        }
        
class BenchmarkingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BenchmarkingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdSc'].queryset = Sector.objects.filter(Eliminado=False)
        self.fields['IdAg'].queryset = AreaGeografica.objects.filter(Eliminado=False)
    class Meta:
        model = Benchmarking
        fields = ['IdSc','IdAg','Nombre','Descripcion','Ciclo','Anyo','Valor']
        labels = {
            'IdSc':'Sector',
            'IdAg':'Área Geográfica',
            'Anyo':'Año'
        }

class PuntosCapituloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PuntosCapituloForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdMd'].queryset = Modelo.objects.filter(Eliminado=False)
        self.fields['IdAm'].queryset = Ambito.objects.filter(Eliminado=False)

    class Meta:
        model = PuntosCapitulo
        fields = ['IdMd','IdAm','Nombre']
        labels = {
            'IdMd':'Modelo',
            'IdAm':'Ámbito'
        }

class ObjetivoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ObjetivoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdTo'].queryset = TipoObjetivo.objects.filter(Eliminado=False)
        self.fields['IdPc'].queryset = PuntosCapitulo.objects.filter(Eliminado=False)
        self.fields['IdParent'].queryset = Objetivo.objects.filter(Eliminado=False)

    class Meta:
        model = Objetivo
        fields = ['IdTo','IdPc','IdParent','Nombre','Descripcion','Codificacion','Anyo']
        labels = {
            'IdTo':'Tipo Objetivo',
            'IdPc':'Puntos Capítulo',
            'IdParent':'Objetivo Padre',
            'Anyo':'Año'
        }

class EstructuraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstructuraForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Estructura
        fields = ['Nombre']

class MetaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MetaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdObj'].queryset = Objetivo.objects.filter(Eliminado=False)
        self.fields['IdParent'].queryset = Meta.objects.filter(Eliminado=False)
    
    class Meta:
        model = Meta
        fields = ['IdObj','IdParent','Codificacion','Nombre','Descripcion']
        labels = {
            'IdObj':'Objetivo',
            'IdParent':'Meta padre'
        }

class AccionMetaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccionMetaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdMeta'].queryset = Meta.objects.filter(Eliminado=False)
    
    class Meta:
        model = AccionMeta
        fields = ['IdMeta','Nombre','Estado','Plazo']
        labels = {
            'IdMeta':'Meta'
        }

class IndicadorAccionProcesoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IndicadorAccionProcesoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdAcc'].queryset = AccionMeta.objects.filter(Eliminado=False)
        self.fields['IdProc'].queryset = Proceso.objects.filter(Eliminado=False)
        
    class Meta:
        model = IndicadorAccionProceso
        fields = ['IdAcc','IdProc','Nombre','Descripcion','Periodo','Estado','ValorObjetivo','ValorConseguido','Plazo']
        labels = {
            'IdAcc':'Accion Meta',
            'IdProc':'Proceso'
        }

class SeguimientoIndicadoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SeguimientoIndicadoresForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdAccMeta'].queryset = IndicadorAccionProceso.objects.filter(Eliminado=False)
        self.fields['IdDoc'].queryset = DocumentosSistema.objects.filter(Eliminado=False)
    
    class Meta:
        model = SeguimientoIndicadores
        fields = ['IdAccMeta','IdDoc','Fecha','Seguimiento']
        labels = {
            'IdAccMeta':'IndicadorAccionProceso',
            'IdDoc':'Documento'
        }

class DocumentosSistemaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentosSistemaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdPc'].queryset = PuntosCapitulo.objects.filter(Eliminado=False)
    
    class Meta:
        model = DocumentosSistema
        fields = ['IdPc','Nombre','Codificacion']
        #fields = '__all__'
        labels = {
            'IdPc':'Puntos Capitulo'
        }

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
class ProcesoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcesoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['IdPc'].queryset = PuntosCapitulo.objects.filter(Eliminado=False)
        self.fields['IdEst'].queryset = Estructura.objects.filter(Eliminado=False)
    
    class Meta:
        model = Proceso
        fields = ['IdPc','IdEst','Nombre','Codificacion']
        labels = {
            'IdPc':'Puntos Capitulo',
            'IdEst':'Estructura'
        }
