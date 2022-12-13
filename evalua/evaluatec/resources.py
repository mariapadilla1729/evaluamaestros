from import_export import resources
from .models import departamento,maestro,carrera,cursos

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = departamento
class MaestroResource(resources.ModelResource):
    class Meta:
        model = maestro
class CarreraResource(resources.ModelResource):
    class Meta:
        model = carrera
class CursosResource(resources.ModelResource):
    class Meta:
        model = cursos