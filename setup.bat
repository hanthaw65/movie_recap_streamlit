@echo off
REM Movie Recap AI - Setup Script for Windows
REM This script automates the installation and setup process

echo ================================
echo Movie Recap AI - Setup Script
echo ================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Found Python %PYTHON_VERSION%

REM Check FFmpeg
echo.
echo Checking FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo Warning: FFmpeg is not installed or not in PATH
    echo Please download FFmpeg from https://ffmpeg.org/download.html
    echo and add it to your PATH
    pause
) else (
    for /f "tokens=*" %%i in ('ffmpeg -version ^| findstr /R "ffmpeg version"') do echo Found: %%i
)

REM Create virtual environment
echo.
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo.
echo Installing dependencies...
echo This may take several minutes...
pip install -r requirements.txt --quiet

REM Create .env file if it doesn't exist
echo.
echo Checking configuration...
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo Warning: Please edit .env and add your Gemini API key
) else (
    echo .env file already exists
)

REM Create necessary directories
echo.
echo Creating directories...
if not exist "temp_files" mkdir temp_files
if not exist "output_files" mkdir output_files
echo Directories created

REM Final message
echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo Next steps:
echo 1. Edit .env file and add your Gemini API key:
echo    notepad .env
echo.
echo 2. Run the application:
echo    streamlit run app.py
echo.
echo 3. Open your browser to http://localhost:8501
echo.
echo For more information, see README.md or QUICKSTART.md
echo.
pause
