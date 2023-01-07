# Importation des librairies nécessaires
import requests
import icmplib
import time

# Définition des constantes
TEST_FILE_URL = "http://ipv4.download.thinkbroadband.com/50MB.zip"
UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"
FILE_PATH = "Application\modules\download\TESTMB.zip"
HOST = "ipv4.download.thinkbroadband.com"

# Définition des fonctions
def get_download_speed(test_file_url=TEST_FILE_URL):
    """
    Calcule la vitesse de téléchargement en mégabits par seconde.
    
    Args:
        test_file_url (str): URL du fichier de test à télécharger.
        
    Returns:
        str: Vitesse de téléchargement en mégabits par seconde, formatée avec 2 chiffres après la virgule.
        
    Raises:
        requests.exceptions.RequestException: Si une erreur se produit lors du téléchargement du fichier de test.
    """
    download_start_time = time.time()
    response = requests.get(test_file_url)
    download_end_time = time.time()
    elapsed_time = download_end_time - download_start_time
    download_speed = len(response.content) / elapsed_time
    return "{0:.2f}".format(download_speed / 1000000 * 8)

def get_upload_speed(file_path=FILE_PATH, upload_url=UPLOAD_URL):
    """
    Calcule la vitesse d'envoi en mégabits par seconde.
    
    Args:
        file_path (str): Chemin d'accès au fichier à envoyer.
        upload_url (str): URL de téléchargement.
        
    Returns:
        str: Vitesse d'envoi en mégabits par seconde, formatée avec 2 chiffres après la virgule.
        
    Raises:
        requests.exceptions.RequestException: Si une erreur se produit lors de l'envoi du fichier.
        FileNotFoundError: Si le fichier spécifié par `file_path` n'existe pas.
    """
    with open(file_path, 'rb') as file:
        upload_start_time = time.time()
        files = {'file': file}
        response = requests.post(upload_url, files=files)
        upload_end_time = time.time()
        upload_speed = len(response.content) / (upload_end_time - upload_start_time)
        return "{0:.2f}".format(upload_speed)

def get_ping(host=HOST):
    """
    Envoie une requête ICMP et renvoie la durée du ping en millisecondes.
    
    Args:
        host (str): Hôte à ping.
        
    Returns:
        int: Durée du ping en millisecondes.
        
    Raises:
        icmplib.exceptions.PingError: Si une erreur se produit lors de l'envoi de la requête ICMP.
    """
    icmp = icmplib.ping(host, count=1)
    ping = int(icmp.avg_rtt)
    return ping

def api_speedtest():
    """
    Calcule la vitesse de téléchargement, d'envoi et de ping.
    
    Returns:
        dict: Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping.
    """
    download_speed = get_download_speed()
    upload_speed = get_upload_speed()
    ping = get_ping()
    result = {"download_speed": download_speed, "upload_speed": upload_speed, "ping": ping}
    print(result)
  

if __name__ == "__main__":
    api_speedtest()




