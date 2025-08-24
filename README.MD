# 📝 Aplicación de Notas con Django

Una aplicación web simple para gestionar notas, creada con Django.

## 🚀 Características

- Crear, ver y eliminar notas
- Interfaz responsive con Bootstrap
- Panel de administración Django

## 🛠️ Tecnologías

- Python 3.12+
- Django 4.2+
- Bootstrap 5
- SQLite

## ⚡ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/django-notas-app.git
Crear entorno virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
.\venv\Scripts\activate  # Windows
Instalar dependencias:

bash
pip install -r requirements.txt
Ejecutar migraciones:

bash
python manage.py migrate
Ejecutar servidor:

bash
python manage.py runserver
Abrir en navegador: http://127.0.0.1:8000

text

## 🔄 **ACTUALIZAR CON EL README**

```bash
git add README.md
git commit -m "Add README.md"
git push
🌐 VISUALIZAR EN GITHUB
Ve a tu repositorio en GitHub

Deberías ver todos los archivos

El README.md se mostrará automáticamente

⚠️ NOTAS IMPORTANTES
NUNCA subas la base de datos (db.sqlite3)

NUNCA subas el entorno virtual (venv/)

El archivo requirements.txt es esencial para que otros puedan instalar las dependencias

El .gitignore es tu mejor amigo para evitar subir archivos innecesarios

🎯 PASOS FINALES
bash
# Verificar estado de Git
git status

# Verificar qué se va a subir
git add -n .  # Muestra qué archivos se agregarán

# Si todo está bien, hacer commit final
git add .
git commit -m "Project ready for deployment"

# Subir a GitHub
git push