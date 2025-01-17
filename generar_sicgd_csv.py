"""
CLI Base de Datos

No deje de configurar la variable de entorno RESPALDOS_BASE_DIR

    # CLI Directorio base donde encontrar los respaldos de la base de datos
    RESPALDOS_BASE_DIR=E:/dir_respaldos
    # NOMBRE_DISTRITO el nombre del distrito donde se encuentra el servidor para hacer diferenciado
"""

import os
import re
import csv
import click

from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()  # Take environment variables from .env

# Cargar variables de entorno
RESPALDOS_BASE_DIR = os.getenv("RESPALDOS_BASE_DIR", "")
NOMBRE_DISTRITO = os.getenv("NOMBRE_DISTRITO", "")


@click.command()
@click.argument("anio_mes", default="0", type=str)
@click.argument("patron_inicio", default="", type=str)
def generar_sicgd_csv(anio_mes, patron_inicio):
    """Generar CSV para SICGD Respaldos BD"""

    # Validar que la variable de entorno este definida
    if RESPALDOS_BASE_DIR is None or RESPALDOS_BASE_DIR == "":
        click.echo("ERROR: Falta la variable de entorno RESPALDOS_BASE_DIR")
        return
    
    # Validar que exista y que sea un directorio
    respaldos_base_dir = Path(RESPALDOS_BASE_DIR)
    if not respaldos_base_dir.exists() or not respaldos_base_dir.is_dir():
        click.echo(f"ERROR: No existe o no es directorio {respaldos_base_dir}")
        return
    
    # Validar que el parámetro mes_int sea YYYY-MM
    if anio_mes == '0':
        anio_mes = datetime.strftime(datetime.now(), "%Y-%m")
    else:
        if not re.match(r"^\d{4}-\d{2}$", anio_mes):
            click.echo(f"ERROR: {anio_mes} no es una fecha valida (YYYY-MM)")
            return

    # Definir el nombre del archivo CSV que se va a escribir
    output = f"reporte_respaldos_bd_{anio_mes}.csv"
    if NOMBRE_DISTRITO != "":
        output = f"reporte_respaldos_bd_{NOMBRE_DISTRITO}_{anio_mes}.csv"

    # Buscar archivos dentro del directorio de respaldo que tengan el nombre buscado
    click.echo("Leyendo archivos de respaldos BD...")
    archivos = []
    fecha_buscada = f"{anio_mes[0:4]}{anio_mes[5:7]}"
    for archivo in respaldos_base_dir.rglob("*"):
        if patron_inicio in archivo.name and fecha_buscada in archivo.name:
            stat = os.stat(archivo)
            patron_fecha = re.search(r"\d{4}\d{2}\d{2}", archivo.name)
            patron_fecha = patron_fecha.group()
            fecha = datetime.strptime(patron_fecha, "%Y%m%d")
            archivo = {
                "fecha": fecha,
                "nombre": archivo.name,
                "tamanio": stat.st_size / (1024 * 1024),
            }
            archivos.append(archivo)
    
    # Si no se encontraron archivos, salir
    if len(archivos) <= 0:
        click.echo("No se generó el archivo porque no se encontraron archivos.")
        return

    # Definir el nombre del archivo CSV que se va a escribir
    output = f"reporte_respaldos_bd_{anio_mes}.csv"
    if NOMBRE_DISTRITO != "":
        output = f"reporte_respaldos_bd_{anio_mes}_{NOMBRE_DISTRITO}.csv"
    ruta = Path(output)

    # Escribir el archivo CSV
    with open(ruta, "w", encoding="utf8") as puntero:
        reporte = csv.writer(puntero)
        reporte.writerow(
            [
                "Fecha",
                "Nombre del archivo",
                "Tamaño",
            ]
        )
        for archivo in archivos:
            reporte.writerow(
                [
                    archivo["fecha"].strftime("%Y-%m-%d"),
                    archivo["nombre"],
                    f"{archivo['tamanio']:.2f}",
                ]
            )

    # Mostrar en pantalla resultado
    fechas = []
    nombres = []
    tamanios = []
    for archivo in archivos:
        fechas.append( archivo['fecha'].strftime('%Y-%m-%d') )
        nombres.append( archivo['nombre'] )
        tamanios.append( f"{archivo['tamanio']:.2f}" )

    # Armado de la tabla
    tabla = tabulate({"Fecha" : fechas, "Nombre": nombres, "Tamanio (MB)" : tamanios}, headers="keys")
    click.echo(tabla)

    # Mostrar mensaje final
    click.echo(f"  {len(archivos)} archivos de respaldo en {ruta.name}")


if __name__ == '__main__':
  generar_sicgd_csv()
