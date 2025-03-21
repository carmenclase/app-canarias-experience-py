# Contactos App

## Descripción

Aplicación Flask y Bootstrap que muestra un listado de los sitios más atractivos de las Islas Canarias.

## Requisitos
- Python 3.9+
- Docker (opcional para despliegue)

## Instalación y ejecución manual

### Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Ejecutar la aplicación

## En la terminal:

```bash
python app.py
```

## Ejecución con Docker

### Construcción de la imagen

```bash
docker build -t app-canarias-experience-py .
```

### Ejecución del contenedor

```bash
docker run -d -p 5000:5000 --name app-canarias-experience-py app-canarias-experience-py
```

Para borrar la caché de Docker Compose:

```bash
docker stop app-canarias-experience-py
docker rm app-canarias-experience-py
```
