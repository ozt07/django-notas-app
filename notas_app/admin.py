from django.contrib import admin
from .models import Nota

# 🎯 Registra el modelo Nota en el panel de administración
# Esto permite crear, editar y eliminar notas desde /admin
admin.site.register(Nota)
