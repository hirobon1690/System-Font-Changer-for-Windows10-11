cd %windir%\Fonts
takeown /F segoeui*.ttc /A
icacls segoeui*.ttf /grant Administrators:F
del segoeui*.ttf
pause