# pjecz-tauro-cli

Script para generar reportes CSV de los respaldos de las base de datos.

## Requerimientos

Los requerimientos son

  - Python 3.14

## Instalación

Crear el entorno virtual de python

`python -m venv .venv`

Activar el entorno virtual desde Windows

`.venv\Scripts\activate`

Instalar el paquete Poetry

`pip install poetry`

Instalar los requerimientos

`poetry install`

Si se desea exportar los paquetes instalados

`poetry export -f requirements.txt --output requirements.txt`

Crear el archivo ejecutable

`python setup.py build`

Se creará una carperta llama build, dentro está el archivo .exe.

## Configuración

Archivo `.env`

```
# Directorio base donde se encuentran los archivos de repaldo
RESPALDOS_BASE_DIR=C:\Users\...
NOMBRE_DISTRITO=Saltillo
```

## Ejecutar CLI

`python generar_sicgd_csv.py 0 Juzgado_`


## Convertir un script Python en un archivo ejecutable

Instalar el paquete `cx_Freeze`

`poetry add cx_Freeze`

Crear el archivo ejecutable

`python setup.py build`