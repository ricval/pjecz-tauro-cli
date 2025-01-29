:: Script para crear Respaldo SQL, comprimirlo, subirlo a GCS.
@echo off
set "nombre_archivo=Juzgado_20250108"


:: Creación de un log de información
echo %date% %time% "Crear, comprimir, subir a GCS y eliminar archivos de respaldo" >> crear_subir_respaldo.log


:: Crear respaldo SQL
echo "Respaldo SQL hecho" >> crear_subir_respaldo.log


:: Comprimir archivo SQL
"C:\Program Files\7-Zip\7z.exe" a "%nombre_archivo%.7z" "%nombre_archivo%.BAK" 2> errores_7zip.log
if %errorlevel% neq 0 (
    echo ERROR al comprimir el archivo. Revisa el archivo errores_7zip.log >> errores_7zip.log
    exit /b %errorlevel% 
)
echo "Respaldo Comprimido" >> crear_subir_respaldo.log


:: Subir archivo comprimido a GCS
echo "Respaldo Subido a GCS" >> crear_subir_respaldo.log


:: Eliminar archivos con más de n días
echo "Eliminando archivos de respaldos" >> crear_subir_respaldo.log

exit