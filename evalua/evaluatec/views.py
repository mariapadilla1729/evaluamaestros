from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import carrera,maestro,departamento,cursos

from django.contrib.auth.forms import UserCreationForm
from evaluatec.forms import carreraform,maestroform,departamentoform,cursosform,Registroform #cursosform,Registroform
import csv,io

from django.contrib import messages 
#from spamanator.utils import get_ip
from django.contrib.auth.decorators import permission_required
#from django.shortcuts import render, redirect,get_object_or_404,render_to_response
from django.http import  HttpResponseNotFound
from django.http import HttpResponse, request

from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
import subprocess, gzip
from subprocess import Popen,run
from evalua.settings import DATABASES
from django.core.files.storage import FileSystemStorage
from django.db import transaction
import json
from django.views import generic
# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import base64
import matplotlib.dates as mdates
from io import BytesIO
from matplotlib.ticker import LinearLocator
import pandas
import numpy
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#from import_export import resources
#from utils import get_plot
# Create your views here.
def check(request):
        try:
            passwd = DATABASES['default']['PASSWORD']#pasword
            user = DATABASES['default']['USER']#nombre Superuser
            use= request.Get.get("username") #usuario q se esta creando aqui  meter nombre caja de text ("ct")
            pasw= request.Get.get("password") #usuario q se esta creando aqui meter el nombre de las cajadetex
            ######## de aqui 
            permisos= request.POST.getlist('perm[]')
            i=len('perm[]')
            if i==0:
                privileges=" "
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==1:
                privileges=" "+permisos[0]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==2:  
                privileges=" "+permisos[0]+","+permisos[1]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==3:
                privileges=" "+permisos[0]+","+permisos[1]+","+permisos[2]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
            if i==4:
                privileges=" "+permisos[0]+","+permisos[1]+","+permisos[2]+","+permisos[3]
                command = "mysql -u"+user+"-p"+passwd+"--init-command=\"GRANT "+ privileges +" ON BDD.* TO '"+use+"'@'localhost' IDENTIFIED BY '"+pasw+"'\""
                subprocess.run(command )
        except :
             print()

        return render(request,"evaluaciontec/permisos.html")

#backup
def backup(request):
    name = DATABASES['default']['NAME']
    passwd = DATABASES['default']['PASSWORD']
    user = DATABASES['default']['USER']
    #mysqldump -u root -p agenda > C:/respaldos/agenda1.sql
    proc = subprocess.Popen("C:/xampp/mysql/bin/mysqldump -u "+user+" -p"+passwd+" "+name+" > "+ "C:/respaldos/backup.sql", shell=True)
    proc.wait()
    procs = subprocess.Popen("tar -czvf "+ "C:/respaldos/backup.tar.tgz "+ "C:/respaldos/backup.sql", shell=True, )
    procs.wait()
    fs = FileSystemStorage("C:/respaldos/")
    with fs.open('backup.tar.tgz') as tar:
        response = HttpResponse(tar, content_type='application/x-gzip')
        response['Content-Disposition'] = 'filename="backup.tar.tgz"'
        return response

def index(request):
    return render(request, 'evaluaciontec/index.html')

#respaldo
def respaldo(request):
    return render(request, 'evaluaciontec/respaldo.html')
    
#############################################################################################################
def main_view(request):
    #qs=cursos.objects.all()
    qs=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2019').order_by('puntaje') 
    qs2=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2020').order_by('puntaje') 
    qs3=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2021').order_by('puntaje') 
    qs4=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2022').order_by('puntaje')
    qs5=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2023').order_by('puntaje')
    qss=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2019').order_by('puntaje') 
    qss2=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2020').order_by('puntaje') 
    qss3=cursos.objects.filter(aspectos='Total').filter(semestre='juldic021').order_by('puntaje') 
    qss4=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2022').order_by('puntaje')
    qss5=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2023').order_by('puntaje')  
    p=[p.idDepartamento for p in qs]
    x=[]
    
    for t,v in enumerate(p):
        if v == 1:
            x.append('Cienecias y Tierra')            
        if v == 2:
            x.append('Economia y Administracion')
        if v == 3:
            x.append('Sistemas y Computacion')
        if v ==4:
            x.append('Electrica y Electronica')
        if v == 5:
            x.append('Mecanica')
        if v == 6:
            x.append('Industrial')
        if v== 7:
            x.append('Ciencias Basicas')
        if v ==8:
            x.append('Idiomas')
           
    #z=[z.semestre for z in qs]    
    y=[y.puntaje for y in qs]
    y2=[y2.puntaje for y2 in qs2]
    y3=[y3.puntaje for y3 in qs3]
    y4=[y4.puntaje for y4 in qs4]
    y5=[y5.puntaje for y5 in qs5]
    y6=[y6.puntaje for y6 in qss]
    y7=[y7.puntaje for y7 in qss2]
    y8=[y8.puntaje for y8 in qss3]
    y9=[y9.puntaje for y9 in qss4]
    y10=[y10.puntaje for y10 in qss5] 
    #y2=[]
    """for u,v in enumerate(y2):
        y2[u]=float(v)+ 1.0  
    #z={z.semestre:departamento}"""
    
    chart=get_plot(x,y,y2,y3,y4,y5,y6,y7,y8,y9,y10, 'Departamentos','Departamento', 'Promedio Total')
    #chart=get_plot(xx,yy)
    return render(request,'evaluaciontec/departamento.html',{'chart':chart})
    #return render(request,'evaluaciontec/departamento.html',)
#######################################
def main_vieww(request):
    #qs=cursos.objects.all()
    qs=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2019').order_by('puntaje') 
    qs2=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2020').order_by('puntaje') 
    qs3=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2021').order_by('puntaje') 
    qs4=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2022').order_by('puntaje')
    qs5=cursos.objects.filter(aspectos='Total').filter(semestre='enjun2023').order_by('puntaje')
    qss=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2019').order_by('puntaje') 
    qss2=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2020').order_by('puntaje') 
    qss3=cursos.objects.filter(aspectos='Total').filter(semestre='juldic021').order_by('puntaje') 
    qss4=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2022').order_by('puntaje')
    qss5=cursos.objects.filter(aspectos='Total').filter(semestre='juldic2023').order_by('puntaje')  
    p=[p.idDepartamento for p in qs]
    x=[]   
    for t,v in enumerate(p):
        if v == 1:
            x.append('Cienecias y Tierra')            
        if v == 2:
            x.append('Economia y Administracion')
        if v == 3:
            x.append('Sistemas y Computacion')
        if v ==4:
            x.append('Electrica y Electronica')
        if v == 5:
            x.append('Mecanica')
        if v == 6:
            x.append('Industrial')
        if v== 7:
            x.append('Ciencias Basicas')
        if v ==8:
            x.append('Idiomas')
           
       
    y=[y.puntaje for y in qs]
    y2=[y2.puntaje for y2 in qs2] 
    y3=[y3.puntaje for y3 in qs3]
    y4=[y4.puntaje for y4 in qs4]
    y5=[y5.puntaje for y5 in qs5]
    y6=[y6.puntaje for y6 in qss]
    y7=[y7.puntaje for y7 in qss2]
    y8=[y8.puntaje for y8 in qss3]
    y9=[y9.puntaje for y9 in qss4]
    y10=[y10.puntaje for y10 in qss5]
    #y2=[]
    """for u,v in enumerate(y2):
        y2[u]=float(v)+ 1.0  
    #z={z.semestre:departamento}"""
    
    chart=getplot(x,y,y2,y3,y4,y5,y6,y7,y8,y9,y10,'Departamentos','Departamento', 'Promedio Total')
    #chart=get_plot(xx,yy)
    return render(request,'evaluaciontec/carreras.html',{'chart':chart})
##
def get_graph():
    buffer= BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png= buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
#####
def get_plot(x,y,y2,y3,y4,y5,y6,y7,y8,y9,y10,titulo,nombrex,nombrey):
    plt.switch_backend('AGG')
    plt.figure(figsize=(15,8))
    plt.title(titulo)
    plt.plot(x,y,label="enjun2019") 
    #plt.annotate('EnJun2019',(x,y))
    plt.plot(x,y2,label="enjun2020")
    plt.plot(x,y3,label="enjun2021") 
    plt.plot(x,y4,label="enjun2022") 
    plt.plot(x,y5,label="enjun2023") 
    plt.plot(x,y6,label="juldic2019") 
    plt.plot(x,y7,label="juldic2020")
    plt.plot(x,y8,label="juldic2021") 
    plt.plot(x,y9,label="juldic2022") 
    plt.plot(x,y10,label="juldic2023")      
    #plt.annotate('EnJun2020',(x,y2))  
    plt.xticks(rotation=45)
    plt.xlabel(nombrex)
    plt.ylabel(nombrey)    
    plt.tight_layout()
    #graph= get_graph()
    fig=get_graph()
    return fig

def getplot(x,y,y2,y3,y4,y5,y6,y7,y8,y9,y10,titulo,nombrex,nombrey):
    plt.switch_backend('AGG')
    plt.figure(figsize=(15,8))
    plt.title(titulo)
    plt.xlabel(nombrex)
    plt.ylabel(nombrey) 
    plt.plot(x,y,'o') 
    plt.plot(x,y2,'o') 
    plt.plot(x,y3,'o') 
    plt.plot(x,y4,'o') 
    plt.plot(x,y5,'o') 
    plt.plot(x,y6,'o') 
    plt.plot(x,y7,'o')
    plt.plot(x,y8,'o') 
    plt.plot(x,y9,'o') 
    plt.plot(x,y10,'o')  
    fig=get_graph
    return fig

#####chart
#################################################################################################################
#descargar 
@permission_required('admin.can_add_log_entry')
def Maestro_download(request):
    items=maestro.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="maestro.csv"'
    writer =csv.writer(response,delimiter=',')
    writer.writerow(['id','plantel','departamento','rfc','curp','apellidoPaterno','apellidoMaterno','nombre','email'])
    for obj in items:
        writer.writerow([obj.idMaestro,obj.plantel,obj.idDepartamento,obj.rfc, obj.curp,obj.apellidoPaterno,obj.apellidoMaterno, obj.nombre,obj.email])
    return response
@permission_required('admin.can_add_log_entry')
def Departamento_download(request):
    items=departamento.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="departamento.csv"'
    writer =csv.writer(response,delimiter=',')
    writer.writerow( ['id','nombre'])
    for obj in items:
        writer.writerow([obj.idDepartamento,obj.nombre])
    return response
@permission_required('admin.can_add_log_entry')
def Carreras_download(request):
    items=carrera.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="carrera.csv"'
    writer =csv.writer(response,delimiter=',')
    writer.writerow( ['id','nombre','departamento'])
    for obj in items:
        writer.writerow([obj.idCarrera,obj.nombre,obj.idDepartamento])
    return response
@permission_required('admin.can_add_log_entry')
def Curso_download(request):
    items=cursos.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="cursos.csv"'
    writer =csv.writer(response,delimiter=',')
    writer.writerow( ['idAspectos','rfc','aspectos','puntaje','calificacion','semestre','idDepartamento'])
    for obj in items:
        writer.writerow([obj.idAspectos,obj.rfc,obj.aspectos,obj.puntaje,obj.calificacion,obj.semestre,obj.idDepartamento])
    return response
######################################################################################################################################
#import
from .resources  import DepartamentoResource,MaestroResource,CarreraResource,CursosResource
"""def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = EmployeeResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')  """
def departamento_import(request): 
    if request.method == 'POST':
        file_format = request.POST['file-format']
        depa_resource = DepartamentoResource()
        dataset = Dataset()
        new_depa = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_depa.read().decode('utf-8'),format='csv')
            result = depa_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_depa.read().decode('utf-8'),format='json')
            # Testing data import
            result = depa_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            depa_resource.import_data(dataset, dry_run=False)
  
    return render(request, 'evaluaciontec/importar.html') 

def maestro_import(request): 
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = MaestroResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'evaluaciontec/importar.html') 

def carrera_import(request): 
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = CarreraResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'evaluaciontec/importar.html') 

def curso_import(request): 
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = CursosResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'evaluaciontec/importar.html')       
############Registrar Usuarios
class RegistrarUsuario(CreateView):
    model = User
    form_class = Registroform
    template_name = 'evaluaciontec/crear_usuario.html'
    success_url = reverse_lazy('login')

class UsuarioList(ListView):
    model = User
    template_name = 'evaluaciontec/consultar_usuario.html'


"""class UsuarioCreate(CreateView):
    model = User
    form_class = Registroform
    template_name = 'evaluaciontec/añadir_usuario.html'
    success_url = reverse_lazy('ver_usuario')

class UsuarioUpdate(UpdateView):
    model = User
    form_class = Registroform
    template_name = 'evaluaciontec/añadir_usuario.html'
    success_url = reverse_lazy('ver_usuario')

class UsuarioDelete(DeleteView):
    model = User
    form_class = Registroform
    template_name = 'evaluacion/eliminar_usuario.html'
    success_url = reverse_lazy('ver_usuario')"""

############################# index
def index(request):
    return render(request, 'evaluaciontec/index.html')
#usuario
class RegistrarUsuario(CreateView):
    model = User
    template_name = 'evaluaciontec/crear_usuario.html'
    form_class = Registroform
    success_url = reverse_lazy('login')
##############################
#Maestros
class MaestroList(ListView):
    model = maestro
    template_name = 'evaluaciontec/consulta_maestro.html'

class MaestroCreate(CreateView):
    model = maestro
    form_class = maestroform
    template_name = 'evaluaciontec/añadir_maestro.html'
    success_url = reverse_lazy('ver_maestro')

class MaestroUpdate(UpdateView):
    model = maestro
    form_class = maestroform
    template_name = 'evaluaciontec/añadir_maestro.html'
    success_url = reverse_lazy('ver_maestro')

class MaestroDelete(DeleteView):
    model = maestro
    form_class = maestroform
    template_name = 'evaluaciontec/eliminar_maestro.html'
    success_url = reverse_lazy('ver_maestro')
#####################
#departamento
class DepartamentoList(ListView):
    model = departamento
    template_name = 'evaluaciontec/consultar_departamento.html'

class DepartamentoCreate(CreateView):
    model = departamento
    form_class =departamentoform
    template_name = 'evaluaciontec/añadir_departamento.html'
    success_url = reverse_lazy('ver_departamento')

class DepartamentoUpdate(UpdateView):
    model = departamento
    form_class = departamentoform
    template_name = 'evaluaciontec/añadir_departamento.html'
    success_url = reverse_lazy('ver_departamento')

class DepartamentoDelete(DeleteView):
    model = departamento
    form_class = departamentoform
    template_name = 'evaluaciontec/eliminar_departamento.html'
    success_url = reverse_lazy('ver_departamento')
#################################
#Carrera
class CarreraList(ListView):
    model = carrera
    template_name = 'evaluaciontec/consultar_carrera.html'

class CarreraCreate(CreateView):
    model = carrera
    form_class = carreraform
    template_name = 'evaluaciontec/añadir_carrera.html'
    success_url = reverse_lazy('ver_carrera')

class CarreraUpdate(UpdateView):
    model = carrera
    form_class = carreraform
    template_name = 'evaluaciontec/añadir_carrera.html'
    success_url = reverse_lazy('ver_carrera')

class CarreraDelete(DeleteView):
    model = carrera
    form_class = carreraform
    template_name = 'evaluaciontec/eliminar_carrera.html'
    success_url = reverse_lazy('ver_carrera')

##################################################
#cursos
class CursoList(ListView):
    model = cursos
    template_name = 'evaluaciontec/consultar_curso.html'
    
#

class CursosCreate(CreateView):
    model = cursos
    form_class = cursosform
    template_name = 'evaluaciontec/añadir_curso.html'
    success_url = reverse_lazy('ver_curso')
#
class CursosUpdate(UpdateView):
    model = cursos
    form_class = cursosform
    template_name = 'evaluaciontec/añadir_curso.html'
    success_url = reverse_lazy('ver_curso')
#
class CursosDelete(DeleteView):
    model = cursos
    form_class = cursosform
    template_name = 'evaluaciontec/eliminar_curso.html'
    success_url = reverse_lazy('ver_curso')

#####################################################################################################
