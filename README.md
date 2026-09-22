# Gestión de Productos

Aplicación web básica desarrollada con Django para fines académicos.

## Requisitos

- Python 3.12
- pip

## Instalación

```cmd
py -3.12 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata datos_iniciales
python manage.py runserver
```

Luego abrir: http://127.0.0.1:8000/

## Base de datos

El proyecto utiliza SQLite mediante el archivo local `db.sqlite3`, que Django crea al ejecutar las migraciones.
