from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Ambito(models.Model):
    id_am=models.AutoField(primary_key=True, db_column="id_Ambito")
    #Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    str_am_nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    str_am_descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="Descripcion")
    bool_am_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "ambitos"

class TipoObjetivo(models.Model):
    id_to=models.AutoField(primary_key=True, db_column="id_Tipo_Objetivo")
    str_to_nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    bool_to_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_objetivos"

class Estructura(models.Model):
    id_est=models.AutoField(primary_key=True, db_column="id_Estructura")
    str_est_nombre=models.CharField(max_length=256, db_column="Nombre")
    bool_est_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "estructuras"

class Riesgo(models.Model):
    id_rg=models.AutoField(primary_key=True, db_column="id_Riesgo")
    str_rg_nombre=models.CharField(max_length=256,db_column="Nombre")
    bool_rg_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "riesgos"

class TipoInterviniente(models.Model):
    id_ti=models.AutoField(primary_key=True, db_column="id_Tipo_Interviniente")
    str_ti_nombre=models.CharField(max_length=256, db_column="Nombre")
    bool_ti_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_intervinientes"

class Sector(models.Model):
    id_sc=models.AutoField(primary_key=True, db_column="id_Sector")
    str_sc_nombre=models.CharField(max_length=256, db_column="Nombre")
    str_sc_descripcion=models.CharField(max_length=256, db_column="Descripcion",null=True, blank=True)
    bool_sc_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "sectores"

class NivelAreaGeografica(models.Model):
    id_nag=models.AutoField(primary_key=True, db_column="id_Nivel_Area")
    num_nag_nivel=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,blank=False, db_column="Nivel")
    str_nag_nombre=models.CharField(max_length=256,null=False,blank=False, db_column="Nombre")
    str_nag_descripcion=models.CharField(max_length=256,null=True,blank=True, db_column="Descripcion")
    bool_nag_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "nivel_areas_geograficas"

class AreaGeografica(models.Model):
    #id_ag es el id del Area geográfica en sí, cada uno tiene el suyo ,es su identificador único
    id_ag=models.AutoField(primary_key=True, db_column="id_AreaGeografica") 
    #id_ag_nag es el id del Nivel de Area Geografica que te indica esa Area geografica en que nivel está
    id_ag_nag=models.ForeignKey(to=NivelAreaGeografica, db_column="id_NivelArea", null=False, blank=False, on_delete=models.PROTECT)
    #id_ag_parent es el id que indica si esta area depende de otra, por ejemplo Palma de mallorca pertenece a Baleares, no? pues pones aquí el ID único de Baleares
    id_ag_parent=models.ForeignKey(to='self', on_delete=models.PROTECT, db_column="id_AreaSuperior", null=True, blank=True)
    #el nombre del registro
    str_ag_nombre=models.CharField(max_length=256, db_column="Nombre", null=False,blank=False)
    #la descripcion del registro
    str_ag_descripcion=models.CharField(max_length=256, db_column="Descripcion", null=True, blank=True)
    #columna que sirve para indicar si se ha eliminado o no
    bool_ag_eliminado=models.BooleanField(default=False, db_column="eliminado")
    #prueba fallida de validacion
    """ def clean(self):
        if self.id_ag_parent < self.end_date:
            raise ValidationError('El Area geografica padre no puede ser inferior a esta.') 
        if self.id_ag_parent == "0":
            self.id_ag_parent = None """
        
    class Meta:
        db_table = "areas_geograficas"
    
class Empresa(models.Model):
    id_emp=models.AutoField(primary_key=True, db_column="id_Empresa")
    id_emp_sc=models.ForeignKey(to=Sector,on_delete=models.CASCADE, null=False, blank=False, db_column="id_Sector")
    id_emp_ag=models.ForeignKey(to=AreaGeografica, on_delete=models.CASCADE, db_column="id_CentroPrincipal", null=False, blank=True)
    str_emp_nombre=models.CharField(max_length=256, db_column="Nombre")
    str_emp_descripcion=models.CharField(max_length=256,db_column="Descripcion", null=True, blank=True)
    bool_emp_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "empresas"

class Benchmarking(models.Model):
    id_bench=models.AutoField(primary_key=True, db_column="id_Bench")
    id_bench_sc=models.ForeignKey(to=Sector, null=True, blank=True, db_column="id_Sector", on_delete=models.PROTECT)
    id_bench_ag=models.ForeignKey(to=AreaGeografica, null=False, blank=False, db_column="id_AreaGeografica", on_delete=models.PROTECT)
    str_bench_nombre=models.CharField(max_length=256, null=True, blank=True, db_column="Nombre")
    str_bench_descripcion=models.CharField(max_length=256, null=False, blank=False, db_column="Descripcion")
    int_bench_valor=models.IntegerField(null=True, blank=True, db_column="Valor")
    int_bench_año=models.IntegerField(null=True, blank=True, db_column="Año")
    str_bench_ciclo=models.CharField(max_length=256,null=True, blank=True, db_column="Ciclo")
    bool_bench_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table: "benchmarkings"


