@echo off
echo ===================================================
echo   Personalized Networking Assistant - GitHub Upload
echo ===================================================
echo.
echo Please create a NEW blank repository on github.com first.
echo.
set /p repo_url="Paste your GitHub repository link (e.g. https://github.com/yourusername/yourrepo.git) and press Enter: "

if "%repo_url%"=="" (
    echo Error: No URL provided. Exiting.
    pause
    exit /b
)

echo.
echo Connecting local files to your GitHub...
git remote remove origin >nul 2>&1
git remote add origin %repo_url%
git branch -M main

echo.
echo Uploading files to GitHub...
git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo Something went wrong. Make sure you entered the correct URL and are logged into GitHub.
) else (
    echo.
    echo Success! Your project has been uploaded to GitHub!
)
echo.
pause
