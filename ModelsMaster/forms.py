from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo, Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo, Estructura, Meta, AccionMeta, Proceso,
 

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
""" class ObjetivoRelacionadoForm(ModelForm):
    class Meta:
        model = ObjetivoRelacionado
        fields = ['id_or_ob','id_or_ob_asociado','str_or_nombre'] """
class EstructuraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstructuraForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Estructura
        fields = ['Nombre']

class MetaForm()