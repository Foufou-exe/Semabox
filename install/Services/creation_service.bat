

REM Path: install\Service.bat

SET PATH_TO_SERVICE= "%~dp0Semabox-API.bat"

sc create SemaAPI-Services binPath= %PATH_TO_SERVICE% start= auto description= "Application python SemaAPI Services port 80" displayname= "SemaAPI Services"

ECHO Service API est installé avec succès !