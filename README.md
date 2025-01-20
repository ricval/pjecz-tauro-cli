# pjecz-tauro-cli

Script CLI para generar reportes de archivos de BD de respaldo en un archivo CSV.

## Crear el entorno virtual de python

`python -m venv .venv`

## Activar el entorno virtual desde Windows

`.venv\Scripts\activate`

## Archivo `.env`

```
# Directorio base donde se encuentran los archivos de repaldo
RESPALDOS_BASE_DIR=C:\Users\...
NOMBRE_DISTRITO=Saltillo
```

## Instalar el paquete Poetry

`pip install poetry`
`poetry init`
`poetry export -f requirements.txt --output requirements.txt`

## Ejecutar CLI

`python generar_sicgd_csv.py 0 Juzgado_`