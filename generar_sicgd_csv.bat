@echo off
setlocal enabledelayedexpansion

echo Elaborador de Reportes SICGD de archivos de base de datos

:: El primer argumento es el año de búsqueda
if "%1" == "" (
    set "anio=%date:~6,4%"
) else (
    set "anio=%1"
)

:: El segundo argumento es el mes de búsqueda
if "%2" == "" (
    set "mes=%date:~3,2%"
) else (
    set "mes=%2"
)
echo La fecha asignada es: %anio%-%mes%

:: Crear archivo de reporte
echo Generando reporte
set "nombre_archivo=reporte_%anio%%mes%.csv"
echo Fecha,"Nombre Archivo","Tamanio (MB)" > %nombre_archivo%

:: Listar archivos con la fecha de búsqueda en su nombre
(
    for /f "tokens=*" %%a in ('dir /b /s *%anio%%mes%*.BAK') do (
        set "nombre_archivo_listado=%%~nxa"
        set "fecha_en_nombre=!nombre_archivo_listado:*%anio%%mes%=!"
        set "dia=!fecha_en_nombre:~0,2!"
        set "fecha=%anio%-%mes%-!dia!"
        set "tamanio=%%~za"
        set /a "tamanioMB=!tamanio! / 1024 / 1024"
            echo !fecha!,%%~nxa,!tamanioMB!
    )
) >> %nombre_archivo%

:: Fin de ejecucion
pause exit
