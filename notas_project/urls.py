from django.contrib import admin
from django.urls import path, include

# 🌐 URLs GLOBALES del proyecto
urlpatterns = [
    # 👨‍💼 Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # 🔗 Incluye todas las URLs de tu aplicación de notas
    path('', include('notas_app.urls')),
]

