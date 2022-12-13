from django.contrib import admin

# Register your models here.
from .models import maestro,carrera,departamento,cursos

# Register your models here.
admin.site.register(maestro)
admin.site.register(carrera)
admin.site.register(departamento)
admin.site.register(cursos)
