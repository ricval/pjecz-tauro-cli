import sys
from cx_Freeze import setup, Executable

# Información de tu aplicación
base = None

setup(  name = "Nombre de mi aplicación",
        version = "0.1",
        description = "Descripción de mi aplicación",
        options = {"build_exe": {"packages":["requests"]}}, 
        executables = [Executable("generar_sicgd_csv.py", base=base)])