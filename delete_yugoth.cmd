cd %windir%\Fonts
takeown /F YuGoth*.ttc /A
icacls YuGoth*.ttc /grant Administrators:F
del YuGoth*.ttc
pause