from django.contrib import admin
from .models import Calculo

@admin.register(Calculo)
class CalculoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'expresion', 'resultado', 'fecha_creacion')
    list_filter = ('usuario', 'fecha_creacion')
    search_fields = ('expresion',)
    readonly_fields = ('fecha_creacion',)