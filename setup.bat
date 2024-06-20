@echo off
echo Setting up the environment...

:: Install necessary Python libraries
pip install -r requirements.txt

:: Check if Wireshark is installed
if exist "C:\Program Files\Wireshark\tshark.exe" (
    echo Wireshark is already installed.
) else (
    echo Installing Wireshark...

    :: First attempt
    powershell -Command "try { Start-Process 'https://2.na.dl.wireshark.org/win64/Wireshark-win64-4.0.1.exe' -ArgumentList '/S' -Wait } catch { exit 1 }"
    if %errorlevel% neq 0 (
        echo First download attempt failed. Trying another URL...
        powershell -Command "try { Start-Process 'https://www.wireshark.org/download/win64/Wireshark-win64-4.0.1.exe' -ArgumentList '/S' -Wait } catch { exit 1 }"
        if %errorlevel% neq 0 (
            echo Second download attempt failed. Trying another URL...
            powershell -Command "try { Start-Process 'https://wireshark.download/automated/win64/Wireshark-win64-4.0.1.exe' -ArgumentList '/S' -Wait } catch { exit 1 }"
            if %errorlevel% neq 0 (
                echo Error: All download attempts failed. Please download and install Wireshark manually from https://www.wireshark.org/download.html
                exit /b 1
            )
        )
    )
)

:: Add Wireshark to PATH
setx path "%path%;C:\Program Files\Wireshark"

:: Verify tshark installation
where tshark
if %errorlevel% neq 0 (
    echo Error: tshark not found. Please ensure Wireshark is installed and added to PATH.
    exit /b 1
)

echo Environment setup complete.
pause
