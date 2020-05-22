from django.db import models
from django.forms import ModelForm
<<<<<<< HEAD
from .models import Ambito, TipoObjetivo, TipoInterviniente, Sector, Nivel_Area_Geografica
=======
from .models import Ambito, TipoObjetivo, Estructura, Riesgo, TipoInterviniente, Sector, NivelAreaGeografica
>>>>>>> 5b9b79a3da05343d2fa92af8e0a749b72643a84d

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['str_am_nombre', 'str_am_descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
<<<<<<< HEAD
        fields = ['Str_Nombre'] 
=======
        fields = ['str_to_nombre'] 

class EstructuraForm(ModelForm):
    class Meta:
        model = Estructura
        fields = ['str_est_nombre' ]

class RiesgoForm(ModelForm):
    class Meta:
        model = Riesgo
        fields = ['str_rg_nombre']
>>>>>>> 5b9b79a3da05343d2fa92af8e0a749b72643a84d

class TipoIntervinienteForm(ModelForm):
    class Meta:
        model = TipoInterviniente
<<<<<<< HEAD
        fields = ['Str_Nombre'] 
=======
        fields = ['str_ti_nombre']
>>>>>>> 5b9b79a3da05343d2fa92af8e0a749b72643a84d

class SectorForm(ModelForm):
    class Meta:
        model = Sector
<<<<<<< HEAD
        fields = ['Str_Sc_Nombre', 'Str_Sc_Descripcion']

class NAGForm(ModelForm):
    class Meta:
        model = Nivel_Area_Geografica
        fields = ['Num_NG_Nivel', 'Str_NG_Nombre', 'Str_NG_Descripcion']
=======
        fields = ['str_sc_nombre', 'str_sc_descripcion']

class NivelAreaGeograficaForm(ModelForm):
    class Meta:
        model = NivelAreaGeografica
        fields = ['num_nag_nivel', 'str_nag_nombre', 'str_nag_descripcion']
>>>>>>> 5b9b79a3da05343d2fa92af8e0a749b72643a84d
