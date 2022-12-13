from django.db import models
# Create your models here.
class departamento(models.Model):
    idDepartamento=models.AutoField(db_column='id', primary_key=True)
    nombre=models.CharField(db_column='nombre', max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'departamento'

class maestro(models.Model):
    idMaestro=models.AutoField(db_column='id', primary_key=True)
    plantel=models.CharField(db_column='plantel', max_length=60,blank=True, null=True)
    idDepartamento= models.ForeignKey('departamento', models.DO_NOTHING,db_column='departamento', blank=True, null=True)
    rfc=models.CharField(db_column='rfc', max_length=13,blank=True, null=True)
    curp=models.CharField(db_column='curp', max_length=19,blank=True, null=True)
    apellidoPaterno=models.CharField(db_column='apellidoPaterno', max_length=20, blank=True, null=True)
    apellidoMaterno=models.CharField(db_column='apellidoMaterno', max_length=20, blank=True, null=True)
    nombre=models.CharField(db_column='nombre', max_length=30, blank=True, null=True)
    email=models.CharField(db_column='email', max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'maestro'
    
class carrera(models.Model):
    idCarrera=models.AutoField(db_column='id', primary_key=True)
    nombre=models.CharField(db_column='nombre', max_length=50, blank=True, null=True) 
    idDepartamento= models.ForeignKey('departamento', models.DO_NOTHING,db_column='departamento', blank=True, null=True)      
    class Meta:
        managed = False
        db_table = 'carrera'

class cursos(models.Model):
    idAspectos=models.AutoField(db_column='idAspectos', primary_key=True)
    rfc=models.CharField(db_column='rfc', max_length=20,blank=True, null=True)
    aspectos= models.CharField(db_column='aspectos', max_length=60,blank=True, null=True)
    puntaje=models.CharField(db_column='puntaje', max_length=3,blank=True, null=True)
    calificacion=models.CharField(db_column='calificacion', max_length=30,blank=True, null=True)
    semestre=models.CharField(db_column='semestre', max_length=40, blank=True, null=True)
    idDepartamento=models.CharField(db_column='idDepartamento', max_length=20, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cursos'
