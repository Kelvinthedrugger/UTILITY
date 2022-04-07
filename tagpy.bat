:: create tags for all python files in that directory and its children
@echo off
set varlist=%1
set pth=%1
for /r %%i in (%pth%*.py) DO call :concat %%i
echo %varlist%
python ptags.py %varlist%
goto :eof

:concat
set varlist=%varlist% %1
goto :eof

