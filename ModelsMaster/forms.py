from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo, Estructura, Riesgo, TipoInterviniente, Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['str_am_nombre', 'str_am_descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['str_to_nombre'] 

class EstructuraForm(ModelForm):
    class Meta:
        model = Estructura
        fields = ['str_est_nombre' ]

class RiesgoForm(ModelForm):
    class Meta:
        model = Riesgo
        fields = ['str_rg_nombre']

class TipoIntervinienteForm(ModelForm):
    class Meta:
        model = TipoInterviniente
        fields = ['str_ti_nombre']

class SectorForm(ModelForm):
    class Meta:
        model = Sector
        fields = ['str_sc_nombre', 'str_sc_descripcion']

class NivelAreaGeograficaForm(ModelForm):
    class Meta:
        model = NivelAreaGeografica
        fields = ['num_nag_nivel', 'str_nag_nombre', 'str_nag_descripcion']

class AreaGeograficaForm(ModelForm):
    class Meta:
        model = AreaGeografica
        fields = ['id_ag_nag','id_ag_parent','str_ag_nombre','str_ag_descripcion']

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['id_emp_sc','id_emp_ag','str_emp_nombre', 'str_emp_descripcion'] 

class ModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['id_md_emp','str_md_nombre','str_md_descripcion']
        
class BenchmarkingForm(ModelForm):
    class Meta:
        model = Benchmarking
        fields = ['id_bench_sc','id_bench_ag','str_bench_nombre','str_bench_descripcion','str_bench_ciclo','int_bench_año','int_bench_valor']

class PuntosCapituloForm(ModelForm):
    class Meta:
        model = PuntosCapitulo
        fields = ['id_pc_md','id_pc_am','str_pc_nombre']

class ObjetivoForm(ModelForm):
    class Meta:
        model = Objetivo
        fields = ['id_ob_to','id_ob_pc','id_ob_parent','str_ob_nombre','str_ob_descripcion','str_ob_codificacion','num_ob_any']

""" class ObjetivoRelacionadoForm(ModelForm):
    class Meta:
        model = ObjetivoRelacionado
        fields = ['id_or_ob','id_or_ob_asociado','str_or_nombre'] """