@echo off

start cmd /k "python manage.py runserver"
timeout /t 3 >nul
start http://127.0.0.1:8000/
