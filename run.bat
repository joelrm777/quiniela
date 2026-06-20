@echo off
title Quiniela Mundial 2026 - Launcher
color 0B

echo ======================================================================
echo           QUINIELA COPA MUNDIAL 2026 - SERVIDORES ACTIVER
echo ======================================================================
echo.
echo [*] Inicializando entorno de ejecucion...
echo [*] Base de datos SQLite y datos de prueba ya cargados.
echo.
echo [*] Abriendo navegador web en http://127.0.0.1:8000/
start http://127.0.0.1:8000/
echo.
echo [*] Iniciando servidor FastAPI con Uvicorn en el puerto 8000...
echo [!] Presiona Ctrl+C para detener el servidor.
echo.

py -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000

pause
