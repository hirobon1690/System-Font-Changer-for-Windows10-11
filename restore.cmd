cd %windir%\Fonts
takeown /F YuGoth*.ttc /A
icacls YuGoth*.ttf /grant Administrators:F
del YuGoth*.ttf
takeown /F SegoeUI*.ttc /A
icacls SegoeUI*.ttf /grant Administrators:F
del SegoeUI*.ttf
pause