[![Django CI](https://github.com/ozt07/django-notas-app/actions/workflows/django-ci.yml/badge.svg)](https://github.com/ozt07/django-notas-app/actions/workflows/django-ci.yml)

# Django Notas App 📝
Una aplicación web desarrollada con Django para gestionar notas personales con funcionalidad de calculadora integrada.

## Características ✨
- ✅ Crear, editar y eliminar notas
- ✅ Interfaz intuitiva y responsive
- ✅ Funcionalidad de calculadora integrada
- ✅ Base de datos SQLite
- ✅ Panel de administración Django
- ✅ Templates HTML organizados
- ✅ Formularios Django para entrada de datos
- ✅ Sistema de routing URL configurado

## Estructura del Proyecto 📁
```
django-notas-app/
├── notas_app/                 # App principal
│   ├── migrations/           # Migraciones de la base de datos
│   ├── templates/notas_app/  # Templates HTML
│   │   ├── base.html
│   │   ├── lista_notas.html
│   │   └── calculadora.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── notas_project/            # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── venv/                     # Entorno virtual
├── db.sqlite3               # Base de datos
├── manage.py
├── requirements.txt
└── .gitignore
```

## Tecnologías Utilizadas 🛠️
- **Backend:** Django 4.2+
- **Frontend:** HTML, CSS, Bootstrap
- **Base de datos:** SQLite3
- **Python:** 3.12+
- **Virtual Environment:** venv
- **Template Engine:** Django Templates

## Instalación y Configuración ⚡

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de instalación

**Clonar el repositorio**
```bash
git clone https://github.com/ozt07/django-notas-app.git
cd django-notas-app
```

**Crear entorno virtual**
```bash
python -m venv venv
```

**Activar entorno virtual**
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**Instalar dependencias**
```bash
pip install -r requirements.txt
```

**Aplicar migraciones**
```bash
python manage.py migrate
```

**Crear superusuario**
```bash
python manage.py createsuperuser
```

**Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

**Acceder a la aplicación**
```
http://localhost:8000/
```

## Uso 🚀
### Para usuarios normales
- 📝 Ver todas las notas: Navega a la página principal
- ➕ Crear nueva nota: Usa el formulario de creación
- ✏️ Editar nota existente: Haz clic en una nota para modificarla
- 🗑️ Eliminar nota: Usa la opción de eliminar
- 🧮 Calculadora: Accede a la pestaña de calculadora para operaciones matemáticas

### Para administradores
- 🔧 Panel admin: Accede a http://localhost:8000/admin
- 👥 Gestionar usuarios: Crear y administrar usuarios
- 📊 Gestionar datos: Administrar todas las notas en la base de datos

## Archivos Importantes 📄
- **models.py** - Define la estructura de la base de datos
- **views.py** - Lógica de la aplicación y controladores
- **urls.py** - Configuración de las rutas URL
- **forms.py** - Formularios para entrada de datos
- **settings.py** - Configuración del proyecto Django

## Comandos Útiles 🖥️
```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test

# Acceder a shell de Django
python manage.py shell
```

## Licencia 📄
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Autor 👨💻
Desarrollado por Tu Nombre

## Contribuciones 🤝
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Automatización con GitHub Actions ⚙️

Este proyecto utiliza GitHub Actions para ejecutar tests automáticos en cada push. El workflow implementado incluye:

### ✅ Funcionalidades del workflow:
- **Ejecución automática** en cada push a la rama main
- **Testing con PostgreSQL** como base de datos de testing
- **Validación de dependencias** con pip
- **Ejecución de migraciones** automáticas
- **Suite de tests** de Django

### 📊 Estado del CI:
![Django CI](https://github.com/ozt07/django-notas-app/actions/workflows/django-ci.yml/badge.svg)

### 🚀 Workflow configuration:
El workflow se encuentra en `.github/workflows/django-ci.yml` y realiza los siguientes pasos:
1. Configura entorno Ubuntu con Python 3.12
2. Instala dependencias del proyecto
3. Configura PostgreSQL para testing
4. Ejecuta migraciones de la base de datos
5. Ejecuta la suite de tests de Django

### 📋 Comandos ejecutados:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py test


## 4. **Comandos para subir los cambios:**

```bash
# Agregar los cambios al README
git add README.md

# Hacer commit
git commit -m "docs: add GitHub Actions badge and documentation"

# Subir a GitHub
git push origin main