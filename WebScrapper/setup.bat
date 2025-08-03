@echo off
title EasyScraper Setup
cls
echo.
echo ========================================
echo    EASYSCRAPER AUTO SETUP
echo ========================================
echo.
echo Installer ini akan:
echo - Mengecek Python installation
echo - Menginstall Python jika belum ada
echo - Menginstall dependencies yang diperlukan
echo - Membuat shortcut untuk menjalankan aplikasi
echo.
pause

echo.
echo [1/4] Mengecek Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Python belum terinstall!
    echo.
    echo Pilihan:
    echo 1. Install Python otomatis
    echo 2. Buka website Python untuk install manual
    echo 3. Keluar
    echo.
    set /p choice="Pilihan Anda (1/2/3): "
    
    if "!choice!"=="1" goto install_python
    if "!choice!"=="2" goto open_python_website
    if "!choice!"=="3" goto exit_setup
    
    echo Pilihan tidak valid!
    pause
    goto exit_setup
    
    :install_python
    echo.
    echo Downloading Python installer...
    
    REM Download Python using PowerShell (works on Windows 7+)
    powershell -Command "try { Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe' -OutFile 'python_installer.exe' } catch { Write-Host 'Download failed. Please install manually.' }"
    
    if exist python_installer.exe (
        echo.
        echo Installing Python...
        python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        echo Waiting for installation to complete...
        timeout /t 45 /nobreak >nul
        del python_installer.exe
        
        REM Refresh environment variables
        call refreshenv.cmd >nul 2>&1
    ) else (
        echo Download failed. Please install Python manually.
        goto open_python_website
    )
    goto check_python_again
    
    :open_python_website
    echo.
    echo Opening Python website...
    start https://www.python.org/downloads/
    echo.
    echo Setelah install Python, jalankan setup ini lagi!
    pause
    goto exit_setup
    
    :check_python_again
    echo.
    echo Checking Python installation again...
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Python installation may have failed.
        echo Please restart command prompt and try again.
        pause
        goto exit_setup
    )
) else (
    echo Python sudah terinstall!
    python --version
)

echo.
echo [2/4] Mengecek pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip tidak ditemukan!
    echo Installing pip...
    python -m ensurepip --upgrade
    if errorlevel 1 (
        echo Failed to install pip automatically.
        echo Please install pip manually.
        pause
        goto exit_setup
    )
) else (
    echo pip sudah tersedia!
)

echo.
echo [3/4] Installing dependencies...
echo Installing required packages...
echo This may take a few minutes...

REM Install packages one by one for better error handling
echo Installing requests...
pip install requests
if errorlevel 1 echo Warning: Failed to install requests

echo Installing beautifulsoup4...
pip install beautifulsoup4
if errorlevel 1 echo Warning: Failed to install beautifulsoup4

echo Installing selenium...
pip install selenium
if errorlevel 1 echo Warning: Failed to install selenium

echo Installing pandas...
pip install pandas
if errorlevel 1 echo Warning: Failed to install pandas

echo Installing lxml...
pip install lxml
if errorlevel 1 echo Warning: Failed to install lxml

echo Installing openpyxl...
pip install openpyxl
if errorlevel 1 echo Warning: Failed to install openpyxl

echo.
echo [4/4] Membuat shortcut...

REM Create simple run script
echo @echo off > run_easyscraper.bat
echo title EasyScraper >> run_easyscraper.bat
echo cd /d "%%~dp0" >> run_easyscraper.bat
echo echo Starting EasyScraper... >> run_easyscraper.bat
echo python easyscraper.py >> run_easyscraper.bat
echo if errorlevel 1 pause >> run_easyscraper.bat

REM Try to create desktop shortcut
echo Creating desktop shortcut...
set "desktop=%USERPROFILE%\Desktop"
if not exist "%desktop%" set "desktop=%HOMEDRIVE%%HOMEPATH%\Desktop"

REM Create VBS script for shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > create_shortcut.vbs
echo sLinkFile = "%desktop%\EasyScraper.lnk" >> create_shortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> create_shortcut.vbs
echo oLink.TargetPath = "%CD%\run_easyscraper.bat" >> create_shortcut.vbs
echo oLink.WorkingDirectory = "%CD%" >> create_shortcut.vbs
echo oLink.Description = "EasyScraper - Web Scraping Tool" >> create_shortcut.vbs
echo oLink.Save >> create_shortcut.vbs

cscript create_shortcut.vbs >nul 2>&1
del create_shortcut.vbs >nul 2>&1

echo.
echo ========================================
echo        SETUP COMPLETED!
echo ========================================
echo.
echo Cara menjalankan EasyScraper:
echo 1. Double-click "EasyScraper" di Desktop
echo 2. Atau double-click "run_easyscraper.bat"
echo 3. Atau buka command prompt dan ketik: python easyscraper.py
echo.
echo File yang dibuat:
echo - run_easyscraper.bat (script untuk menjalankan)
echo - EasyScraper.lnk (shortcut di desktop)
echo.
echo Selamat! EasyScraper siap digunakan!
echo.

REM Test run option
set /p test="Test menjalankan aplikasi sekarang? (y/n): "
if /i "%test%"=="y" (
    echo.
    echo Launching EasyScraper...
    python easyscraper.py
)

:exit_setup
echo.
echo Terima kasih telah menggunakan EasyScraper!
pause