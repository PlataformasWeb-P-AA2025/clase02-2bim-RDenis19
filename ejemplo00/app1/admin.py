from django.contrib import admin

# Importar las clases del modelo
from app1.models import Estudiante
from app1.models import Ciudad

admin.site.register(Estudiante)
admin.site.register(Ciudad)
