from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo, TipoInterviniente, Sector, Nivel_Area_Geografica

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['Str_Nombre', 'Str_Descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['Str_Nombre'] 

class TipoIntervinienteForm(ModelForm):
    class Meta:
        model = TipoInterviniente
        fields = ['Str_Nombre'] 

class SectorForm(ModelForm):
    class Meta:
        model = Sector
        fields = ['Str_Sc_Nombre', 'Str_Sc_Descripcion']

class NAGForm(ModelForm):
    class Meta:
        model = Nivel_Area_Geografica
        fields = ['Num_NG_Nivel', 'Str_NG_Nombre', 'Str_NG_Descripcion']