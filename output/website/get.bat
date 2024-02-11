@echo off
set "DriverPath=%PROGRAMFILES%\Microsoft SQL Server\Client SDK\ODBC\170\SDK"

if exist "%DriverPath%" (
    echo ODBC Driver Header Files Path: %DriverPath%
) else (
    echo ODBC Driver Header Files not found.
)

pause
