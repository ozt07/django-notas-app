from django.urls import path
from . import views

app_name = 'notas_app'

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('borrar-historial/', views.borrar_historial, name='borrar_historial'),
]