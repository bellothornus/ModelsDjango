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
    Id=models.AutoField(primary_key=True, db_column="TO_Id_Tipo_Objetivo")
    Nombre=models.CharField(max_length=256, null=False, blank=False, db_column="TO_Nombre")
    Eliminado=models.BooleanField(default=False, db_column="TO_Eliminado")

    class Meta:
        db_table = "tipos_objetivos"

""" class Estructura(models.Model):
    Id=models.AutoField(primary_key=True, db_column="ES_Id_Estructura")
    Nombre=models.CharField(max_length=256, db_column="ES_Nombre")
    Eliminado=models.BooleanField(default=False, db_column="ES_Eliminado")

    class Meta:
        db_table = "estructuras" """

""" class Riesgo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="RG_Id_Riesgo")
    Nombre=models.CharField(max_length=256,db_column="RG_Nombre")
    Eliminado=models.BooleanField(default=False, db_column="RG_Eliminado")

    class Meta:
        db_table = "riesgos" """

""" class TipoInterviniente(models.Model):
    Id=models.AutoField(primary_key=True, db_column="id_Tipo_Interviniente")
    Nombre=models.CharField(max_length=256, db_column="Nombre")
    Eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_intervinientes" """

class Sector(models.Model):
    Id=models.AutoField(primary_key=True, db_column="SC_Id_Sector")
    Nombre=models.CharField(max_length=256, db_column="SC_Nombre")
    Descripcion=models.CharField(max_length=256, db_column="SC_Descripcion",null=True, blank=True)
    Eliminado=models.BooleanField(default=False, db_column="SC_Eliminado")

    class Meta:
        db_table = "sectores"

class NivelAreaGeografica(models.Model):
    Id=models.AutoField(primary_key=True, db_column="NG_Id_Nivel_Area_Geo")
    Nivel=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,blank=False, db_column="NG_Nivel")
    Nombre=models.CharField(max_length=256,null=False,blank=False, db_column="NG_Nombre")
    Descripcion=models.CharField(max_length=256,null=True,blank=True, db_column="NG_Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="NG_Eliminado")

    class Meta:
        db_table = "nivel_areas_geograficas"

class AreaGeografica(models.Model):
    #id_ag es el id del Area geográfica en sí, cada uno tiene el suyo ,es su identificador único
    Id=models.AutoField(primary_key=True, db_column="AG_Id_Area_Geo") 
    #id_ag_nag es el id del Nivel de Area Geografica que te indica esa Area geografica en que nivel está
    IdNag=models.ForeignKey(to=NivelAreaGeografica, db_column="AG_Id_Nivel", null=False, blank=False, on_delete=models.DO_NOTHING)
    #id_ag_parent es el id que indica si esta area depende de otra, por ejemplo Palma de mallorca pertenece a Baleares, no? pues pones aquí el ID único de Baleares
    IdParent=models.ForeignKey(to='self', on_delete=models.DO_NOTHING, db_column="AG_Id_Area_Padre", null=True, blank=True)
    #el nombre del registro
    Nombre=models.CharField(max_length=256, db_column="AG_Nombre", null=False,blank=False)
    #la descripcion del registro
    Descripcion=models.CharField(max_length=256, db_column="AG_Descripcion", null=True, blank=True)
    #columna que sirve para indicar si se ha eliminado o no
    Eliminado=models.BooleanField(default=False, db_column="AG_Eliminado")
    #prueba fallida de validacion
    """ def clean(self):
        if self.id_ag_parent < self.end_date:
            raise ValidationError('El Area geografica padre no puede ser inferior a esta.') 
        if self.id_ag_parent == "0":
            self.id_ag_parent = None """
        
    class Meta:
        db_table = "areas_geograficas"
    
class Empresa(models.Model):
    Id=models.AutoField(primary_key=True, db_column="EM_Id_Empresa")
    IdSc=models.ForeignKey(to=Sector,on_delete=models.DO_NOTHING, null=False, blank=False, db_column="EM_Id_Sector")
    IdAg=models.ForeignKey(to=AreaGeografica, on_delete=models.DO_NOTHING, db_column="Em_Centro_Principal", null=False, blank=True)
    Nombre=models.CharField(max_length=256, db_column="EM_Nombre")
    Descripcion=models.CharField(max_length=256,db_column="EM_Descripcion", null=True, blank=True)
    Eliminado=models.BooleanField(default=False, db_column="EM_Eliminado")

    class Meta:
        db_table = "empresas"

class Modelo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="MD_Id_Modelo")
    IdEmp=models.ForeignKey(to=Empresa, on_delete=models.DO_NOTHING, db_column="MD_Id_Empresa")
    Nombre=models.CharField(max_length=256, db_column="MD_Nombre")
    Descripcion=models.CharField(max_length=256, blank=True, null=True, db_column="MD_Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="MD_Eliminado")
    
    class Meta:
        db_table= "modelos"
        
class Benchmarking(models.Model):
    Id=models.AutoField(primary_key=True, db_column="BH_Id_Bench")
    IdSc=models.ForeignKey(to=Sector, db_column="BH_Id_Sector", on_delete=models.DO_NOTHING)
    IdAg=models.ForeignKey(to=AreaGeografica, db_column="BH_Id_Area_Geo", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="BH_Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="BH_Descripcion")
    Valor=models.IntegerField(null=True, blank=True, db_column="BH_Valor")
    Anyo=models.IntegerField(null=True, blank=True, db_column="BH_Año")
    Ciclo=models.CharField(max_length=256,null=True, blank=True, db_column="BH_Ciclo")
    Eliminado=models.BooleanField(default=False, db_column="BH_Eliminado")
    
    class Meta:
        db_table = "benchmarkings"

class PuntosCapitulo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="CP_Id_Capitulo")
    IdMd=models.ForeignKey(to=Modelo, db_column="CP_Id_Modelo", on_delete=models.DO_NOTHING)
    IdAm=models.ForeignKey(to=Ambito, to_field='Id', db_column="CP_Id_Ambito", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="CP_Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="CP_Descripcion")
    Eliminado=models.BooleanField(default=False, db_column="CP_Eliminado")

    class Meta:
        db_table = "puntos_capitulos"

class Objetivo(models.Model):
    Id=models.AutoField(primary_key=True, db_column="OB_Id_Objetivo")
    IdPc=models.ForeignKey(to=PuntosCapitulo, db_column="OB_Id_Capitulo", on_delete=models.DO_NOTHING)
    IdTo=models.ForeignKey(to=TipoObjetivo, db_column="OB_Id_Tipo_Objetivo", on_delete=models.DO_NOTHING)
    IdParent=models.ForeignKey(to="self", default="", db_column="OB_Id_Objetivo_Padre", on_delete=models.DO_NOTHING)
    Nombre=models.CharField(max_length=256, db_column="OB_Nombre")
    Descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="OB_Descripcion")
    Codificacion=models.CharField(max_length=256, db_column="OB_Codificacion")
    Anyo=models.IntegerField(null=True, blank=True, db_column="OB_Año")
    Eliminado=models.BooleanField(default=False, db_column="OB_Eliminado")

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