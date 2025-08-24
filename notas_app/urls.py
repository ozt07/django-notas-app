from django.urls import path
from . import views

# 🗺️ URLS: Define las rutas de la aplicación
urlpatterns = [
    # 🏠 Página principal - muestra lista de notas
    path('', views.lista_notas, name='lista_notas'),
    
    # ➕ Página para crear nueva nota
    path('nueva/', views.nueva_nota, name='nueva_nota'),
    
    # 🗑️ Ruta para eliminar nota (con ID dinámico)
    path('eliminar/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'),
]