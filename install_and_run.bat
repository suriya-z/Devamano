@echo off
echo =========================================
echo Devamano Auto-Installer and Runner
echo =========================================
echo.
echo Installing Python dependencies...
pip install -r requirements.txt
echo.
echo =========================================
echo Starting the Devamano Web Server...
echo =========================================
python app.py
pause
