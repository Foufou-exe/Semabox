# Vérifier si Chocolatey est installé
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    # Télécharger et installer Chocolatey
    Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

if (Get-Command nmap.exe -ErrorAction SilentlyContinue) {
    Write-Host "Nmap est installé !"
} else {
    Write-Host "Nmap n'a pas pu être installé."
    # Installer Nmap avec Chocolatey
    choco install nmap
}

