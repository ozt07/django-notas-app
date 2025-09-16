# Imagen base ligera de Python
FROM python:3.12-slim

# Directorio de trabajo dentro del container
WORKDIR /app

# Copiar dependencias primero (optimiza el build)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al container
COPY . .

# Exponer puerto de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
