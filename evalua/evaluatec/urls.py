from django.urls import path
#from django.conf.urls import url
from .views import check,index
from django.contrib.auth.decorators import login_required
from .views import  MaestroList #, MaestroCreate, MaestroDelete,MaestroUpdate
from .views import  DepartamentoList #,DepartamentoCreate,DepartamentoDelete,DepartamentoUpdate
from .views import CarreraList #,CarreraCreate,CarreraDelete,CarreraUpdate
from .views import CursoList #, CursosCreate,CursosUpdate,CarreraDelete
from .views import backup, main_view,main_vieww,respaldo,RegistrarUsuario
from .views import Maestro_download, Departamento_download,Carreras_download,Curso_download
from .views import departamento_import,curso_import,carrera_import,maestro_import

urlpatterns = [
    path('',login_required(index)),  # type: ignore
    path('check', check, name='check'),
    path('respaldo.html',login_required(respaldo)),
    #path('crear_usuario.html',RegistrarUsuario.as_view()),  
    path('consulta_maestro.html',login_required(MaestroList.as_view()),name='ver_maestro'),
    path('consultar_departamento.html',login_required(DepartamentoList.as_view()),name='ver_departamento'),
    path('consultar_carrera.html',login_required(CarreraList.as_view()),name='ver_carrera'),
    path('consultar_curso.html' ,login_required(CursoList.as_view()),name='ver_curso'), 
    path('respalda.html', backup, name='backup'),
    path('departamento.html',main_view,name="main_view"), 
    path('carreras.html',main_vieww,name="main_vieww"), 
    path('descargaMaestro', Maestro_download , name='Maestro_download'),
    path('descargaDepartamento', Departamento_download , name='Departamento_download'),
    path('descargaCarrera', Carreras_download , name='Carreras_download'),
    path('descargaCurso', Curso_download , name='Curso_download'),
    path('importar.html', departamento_import , name='departamento_import'),
    path('importar.html', carrera_import , name='carrera_import'), 
    path('importar.html', curso_import , name='curso_import'),  
    path('importar.html', maestro_import , name='maestro_import'),       
] 
"""
#path('añadir_usuario',login_required(RegistrarUsuario.as_view())), 

    #path('añadir_maestro',login_required(MaestroCreate.as_view())),
    
    #url(r'^modificar_maestro/(?P<pk>\d+)/$',login_required(MaestroUpdate.as_view()), name= 'modi_maestro'),
    #url(r'^eliminar_maestro/(?P<pk>\d+)/$',login_required(MestroDelete.as_view()), name= 'eli_maestro'),
    #path('añadir_departamento',login_required(DepartamentoCreate.as_view())),
    
    #url(r'^modificar_departamento/(?P<pk>\d+)/$',login_required(DepartamentoUpdate.as_view()), name= 'modi_departamento'),
    #url(r'^eliminar_departamento/(?P<pk>\d+)/$',login_required(DepartamentoDelete.as_view()), name= 'eli_departamento'), 
    #path('añadir_carrera',login_required(CarreraCreate.as_view())),
   
    #url(r'^modificar_carrera/(?P<pk>\d+)/$',login_required(CarreraUpdate.as_view()), name= 'modi_carrera'),
    #url(r'^eliminar_carrera/(?P<pk>\d+)/$',login_required(CarreraDelete.as_view()), name= 'eli_carrera'), 
    #path('añadir_curso',login_required(CursosCreate.as_view())),
"""