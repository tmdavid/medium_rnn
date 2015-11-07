REM configuration of paths
set VSFORPYTHON="C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python\9.0"
set SCISOFT=%~dp0

REM add tdm gcc stuff
set PATH=%SCISOFT%\TDM-GCC-64\bin;%SCISOFT%\TDM-GCC-64\x86_64-w64-mingw32\bin;%PATH%

REM add winpython stuff
CALL %SCISOFT%\WinPython-64bit-2.7.10.2\scripts\env.bat

REM configure path for msvc compilers
REM for a 32 bit installation change this line to
REM CALL %VSFORPYTHON%\vcvarsall.bat
CALL %VSFORPYTHON%\vcvarsall.bat amd64

REM return a shell
cmd.exe /k
