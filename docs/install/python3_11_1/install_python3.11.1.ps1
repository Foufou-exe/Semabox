# Description: Install Python 3.11.1

# Fonctions
Function Install-Python {
    param (
        [string]$version_URL = "3.11.1",
        [string]$install_dir = "$env:LOCALAPPDATA\Programs\Python\Python${version_URL}"
    )
    $version = "3.11.1"
    $filename = "python-$version-amd64.exe"
    $url = "https://www.python.org/ftp/python/${version_URL}/${filename}"


    # Téléchargement et installation de Python
    $client = [System.Net.WebClient]::new()
    $request = [System.Net.WebRequest]::Create($url)
    $request.Method = "HEAD"
    $response = $request.GetResponse()
    $totalBytes = $response.ContentLength

    $client.DownloadFileAsync($url, $filename)
    while ((Get-ChildItem $filename).Length -lt $totalBytes) {
        Write-Progress -Activity "Téléchargement de Python" -Status "Percent Complete" -PercentComplete ((Get-ChildItem $filename).Length / $totalBytes * 100)
        Start-Sleep -Milliseconds 100
    }

    Start-Process $filename "/quiet InstallAllUsers=0 TargetDir='$install_dir'" -Wait

    # Ajout de Python au PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";$install_dir"


    # Vérification de l'installation
    Write-Host "Python installé : $python_version" -ForegroundColor Yellow
}

$python_version = Get-Command python -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Version

if ($null -eq $python_version) {
    Write-Host "Python n'est pas installé :( " -ForegroundColor Red
    Install-Python        
}

elseif ($python_version -lt "3.11.1") {
    Write-Host "Python n'est pas à jour :( " -ForegroundColor Red
    Write-Host "Voulez-vous installer la version $version ?" -ForegroundColor Yellow
    $answer = Read-Host "O/N"
    if ($answer -eq "O") {
        Install-Python
    } else {
        Write-Host "Installation annulée." -ForegroundColor Red
    } 
    Install-Python   
}
else {
    Write-Host "Python est déjà à jours avec la version $python_version :)" -ForegroundColor Green
}

