# Contactos App

## Descripción

Aplicación Flask y Bootstrap que muestra un listado de los sitios más atractivos de las Islas Canarias.

## Requisitos
- Python 3.9+
- Docker (opcional para despliegue)

## Instalación y ejecución manual

### Crear entorno virtual e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Ejecutar la aplicación

## En la terminal:

```bash
python3 app.py
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

### Probar la aplicación en local

Acceder a la URL http://localhost:5000 a través del navegador web:

A travé de la terminal ejecutar el comando `curl`:

```bash
curl http://localhost:5000
```