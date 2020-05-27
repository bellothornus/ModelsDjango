from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Ambito(models.Model):
    Id=models.AutoField(primary_key=True,db_column="AM_Id_Ambito")
    Nombre=models.CharField(max_length=256, null=False, blank=False, db_column="AM_Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="AM_Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="AM_Eliminado")

    class Meta:
        db_table = "ambitos"

class TipoObjetivo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Tipo_Objetivo")
    Nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_objetivos"

class Estructura(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Estructura")
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "estructuras"

class Riesgo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Riesgo")
    Nombre=models.CharField(max_length=256,db_column="Nombre")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "riesgos"

class TipoInterviniente(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Tipo_Interviniente")
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_intervinientes"

class Sector(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Sector")
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Descripcion=models.CharField(max_length=256, db_column="Descripcion",null=True, blank=True)
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "sectores"

class NivelAreaGeografica(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Nivel_Area")
    Nivel=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,blank=False, db_column="Nivel")
    Nombre=models.CharField(max_length=256,null=False,blank=False, db_column="Nombre")
    Descripcion=models.CharField(max_length=256,null=True,blank=True, db_column="Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "nivel_areas_geograficas"

class AreaGeografica(models.Model):
    #id_ag es el id del Area geográfica en sí, cada uno tiene el suyo ,es su identificador único
    Id=models.AutoField(primary_key=True, db_column="id_AreaGeografica") 
    #id_ag_nag es el id del Nivel de Area Geografica que te indica esa Area geografica en que nivel está
    IdNag=models.ForeignKey(to=NivelAreaGeografica, db_column="id_NivelArea", null=False, blank=False, on_delete=models.DO_NOTHING)
    #id_ag_parent es el id que indica si esta area depende de otra, por ejemplo Palma de mallorca pertenece a Baleares, no? pues pones aquí el ID único de Baleares
    IdParent=models.ForeignKey(to='self', on_delete=models.DO_NOTHING, db_column="id_AreaSuperior", null=True, blank=True)
    #el nombre del registro
    Nombre=models.CharField(max_length=256, db_column="Nombre", null=False,blank=False)
    #la descripcion del registro
    Descripcion=models.CharField(max_length=256, db_column="Descripcion", null=True, blank=True)
    #columna que sirve para indicar si se ha eliminado o no
    Eliminado=models.BooleanField(default=False, db_column="eliminado")
    #prueba fallida de validacion
    """ def clean(self):
        if self.id_ag_parent < self.end_date:
            raise ValidationError('El Area geografica padre no puede ser inferior a esta.') 
        if self.id_ag_parent == "0":
            self.id_ag_parent = None """
        
    class Meta:
        db_table = "areas_geograficas"
    
class Empresa(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Empresa")
    IdSc=models.ForeignKey(to=Sector,on_delete=models.DO_NOTHING, null=False, blank=False, db_column="id_Sector")
    IdAg=models.ForeignKey(to=AreaGeografica, on_delete=models.DO_NOTHING, db_column="id_CentroPrincipal", null=False, blank=True)
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Descripcion=models.CharField(max_length=256,db_column="Descripcion", null=True, blank=True)
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "empresas"

class Modelo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Modelo")
    IdEmp=models.ForeignKey(to=Empresa, on_delete=models.DO_NOTHING, db_column="id_Empresa")
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Descripcion=models.CharField(max_length=256, blank=True, null=True, db_column="Descripcion")
    Eliminado=models.BooleanField(default=False)
    
    class Meta:
        db_table= "modelos"
        
class Benchmarking(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Bench")
    IdSc=models.ForeignKey(to=Sector, db_column="id_Sector", on_delete=models.DO_NOTHING)
    IdAg=models.ForeignKey(to=AreaGeografica, db_column="id_AreaGeografica", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="Descripcion")
    Valor=models.IntegerField(null=True, blank=True, db_column="Valor")
    Anyo=models.IntegerField(null=True, blank=True, db_column="Año")
    Ciclo=models.CharField(max_length=256,null=True, blank=True, db_column="Ciclo")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")
    
    class Meta:
        db_table = "benchmarkings"

class PuntosCapitulo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Capitulo")
    IdMd=models.ForeignKey(to=Modelo, db_column="id_Modelo", on_delete=models.DO_NOTHING)
    IdAm=models.ForeignKey(to=Ambito, to_field='Id', db_column="id_Ambito", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "puntos_capitulos"

class Objetivo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Objetivo")
    IdPc=models.ForeignKey(to=PuntosCapitulo, db_column="id_Capitulo", on_delete=models.DO_NOTHING)
    IdTo=models.ForeignKey(to=TipoObjetivo, db_column="id_Tipo_Objetivo", on_delete=models.DO_NOTHING)
    IdParent=models.ForeignKey(to="self", default="", db_column="Id_Objetivo_Padre", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="Descripcion")
    Codificacion=models.CharField(max_length=256, db_column="Codificacion")
    Anyo=models.IntegerField(null=True, blank=True, db_column="Año")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "objetivos"

""" class ObjetivoRelacionado(models.Model):
    id_or=models.AutoField(primary_key=True, db_column="id_ObjetivoRelacionado")
    id_or_ob=models.ForeignKey(to=Objetivo, related_name="Id_Objetivo", db_column="id_Objetivo", on_delete=models.DO_NOTHING)
    id_or_ob_asociado=models.ForeignKey(to=Objetivo, related_name="Id_ObjetivoAsociado", db_column="id_Objetivo_Asociado", on_delete=models.DO_NOTHING)
    str_or_nombre=models.CharField(max_length=256, null=True, blank=True, db_column="Nombre")
    bool_or_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "objetivo_relacionado"
 """