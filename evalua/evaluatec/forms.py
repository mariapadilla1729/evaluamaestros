from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import maestro,departamento
from .models import carrera, cursos

#departamento
class departamentoform(forms.ModelForm):
    class Meta:
        model = departamento
        fields = [
            'idDepartamento',
            'nombre',
        ]
        labels = {
            'idDepartamento' : 'idDepartamento',
            'nombre' : 'nombre',
        }
        widgets = {
            'idDepartamento' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),            
        }

#maestro
class maestroform(forms.ModelForm):
    class Meta:
        model = maestro
        fields = [
            'idMaestro',
            'plantel',
            'idDepartamento',
            'rfc',
            'curp',
            'apellidoPaterno',
            'apellidoMaterno',
            'nombre',
            'email',
        ]
        labels = {
            'idMaestro' : 'idMaestro',
            'plantel' : 'plantel',
            'idDepartamento' : 'idDepartamento',
            'rfc' : 'rfc' ,
            'curp' : 'curp',
            'apellidoPaterno' : 'apellidoPaterno',
            'apellidoMaterno' : 'apellidoMaterno',
            'nombre' : 'nombre',
            'email' : 'email',
            
        }
        widgets = {
            'idMaestro' : forms.TextInput(attrs={'class':'form-control'}),             
            'plantel' : forms.TextInput(attrs={'class':'form-control'}),
            'idDepartamento' : forms.TextInput(attrs={'class':'form-control'}),
            'rfc' : forms.TextInput(attrs={'class':'form-control'}),
            'curp' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidoPaterno' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidoMaterno' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),            
        }

#carrera
class carreraform(forms.ModelForm):
    class Meta:
        model = carrera
        fields = [
            'idCarrera',
            'nombre',
            'idDepartamento'
        ]
        labels = {
            'idCarrera' : 'idCarrera',
            'nombre' : 'nombre',
            'idDepartamento' : 'idDepartamento',
        }
        widgets = {
            'idCarrera' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'idDepartamento' : forms.TextInput(attrs={'class':'form-control'}),            
        }

#cursos
class cursosform(forms.ModelForm):
    class Meta:
        model = cursos
        fields = [
            'idAspectos',
            'rfc',
            'aspectos',            
            'puntaje',
            'calificacion',            
            'semestre',
            'idDepartamento'
        ]
        labels = {
            'idAspectos': 'idAspectos',
            'rfc': 'rfc',
            'aspectos':'aspectos',         
            'puntaje': 'puntaje',
            'calificacion': 'calificacion',          
            'semestre': 'semestre',
            'idDepartamento' :'idDepartamento' ,
        }
        widgets = {
            'idAspectos': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'aspectos': forms.TextInput(attrs={'class':'form-control'}),         
            'puntaje': forms.TextInput(attrs={'class':'form-control'}), 
            'calificacion': forms.TextInput(attrs={'class':'form-control'}),          
            'semestre': forms.TextInput(attrs={'class':'form-control'}),
            'idDepartamento' : forms.TextInput(attrs={'class':'form-control'}),          
        }  


#usuario personalizado de django
class Registroform(UserCreationForm):    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre de pila',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
        }