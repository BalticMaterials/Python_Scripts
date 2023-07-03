@echo off
rem ProgramName - short description

set version=1.0.0

rem Determine the folder that the script exists in
rem - used so that all files can be relative to the location
set scriptFolder=%~dp0
rem Remove trailing \ from scriptFolder
set scriptFolder=%scriptFolder:~0,-1%
set scriptName=%~nx0

rem Parse command line using simple approach
if "%1%"=="/h" goto printUsage
if "%2%"=="/h" goto printUsage

rem Insert logic here.

rem Call a function, just have `call` at the front.
call :function1 args...

rem Example function
:function1
rem Some logic here
rem return from the function
exit /b 0

rem Print program usage
:printUsage
echo.
echo Usage here...
goto exit0

rem Final exit
:exit0
exit /b 0