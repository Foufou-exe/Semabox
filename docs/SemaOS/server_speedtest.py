#!/usr/bin/env python3.11.1



# Définition des variables
TEST_FILE_URL = "http://ipv4.download.thinkbroadband.com/50MB.zip" # Fichier de 50 MB
UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media" # URL de téléchargement

# Condition pour le chemin d'accès au fichier
if os.name == 'nt' : # Windows
    FILE_PATH = "SemaOS\download\TESTMB.zip"
else: # Linux ou autre
    FILE_PATH = "SemaOS/download/TESTMB.zip"

HOST = "google.com" # Hôte à ping

# Définition des fonctions
def get_download_speed(test_file_url=TEST_FILE_URL)->str:
    """
    Calcule la vitesse de téléchargement en mégabits par seconde.
    
    Args:
        test_file_url (str): URL du fichier de test à télécharger.
        
    Returns:
        str: Vitesse de téléchargement en mégabits par seconde, formatée avec 2 chiffres après la virgule.
        
    Raises:
        requests.exceptions.RequestException: Si une erreur se produit lors du téléchargement du fichier de test.
    """
    download_start_time = time.time() # Début du téléchargement
    response = requests.get(test_file_url) # Téléchargement du fichier
    download_end_time = time.time() # Fin du téléchargement
    elapsed_time = download_end_time - download_start_time # Durée du téléchargement
    download_speed = len(response.content) / elapsed_time # Vitesse de téléchargement
    return "{0:.2f}".format(download_speed / 1000000 * 8) # Retourne la vitesse de téléchargement en mégabits par seconde

def get_upload_speed(file_path=FILE_PATH, upload_url=UPLOAD_URL)->str:
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
    with open(file_path, 'rb') as file: # Ouverture du fichier
        upload_start_time = time.time() # Début timer de l'envoi
        files = {'file': file} # Fichier à envoyer
        response = requests.post(upload_url, files=files) # Envoi du fichier
        upload_end_time = time.time() # Fin timer de l'envoi
        upload_speed = len(response.content) / (upload_end_time - upload_start_time) # Vitesse d'envoi
        return "{0:.2f}".format(upload_speed) # Retourne la vitesse d'envoi en mégabits par seconde

def get_ping(host=HOST)->int:
    """
    Envoie une requête ICMP et renvoie la durée du ping en millisecondes.
    
    Args:
        host (str): Hôte à ping.
        
    Returns:
        int: Durée du ping en millisecondes.
        
    Raises:
        icmplib.exceptions.PingError: Si une erreur se produit lors de l'envoi de la requête ICMP.
    """
    icmp = icmplib.ping(host, count=1) # Envoi de la requête ICMP, une seule fois
    ping = int(icmp.avg_rtt) # Durée du ping
    return ping # Retourne la durée du ping en millisecondes

def api_speedtest()->dict:
    """
    Calcule la vitesse de téléchargement, d'envoi et de ping.
    
    Returns:
        dict: Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping.
    """
    download_speed = get_download_speed() # Vitesse de téléchargement
    upload_speed = get_upload_speed() # Vitesse d'envoi
    ping = get_ping() # Ping
    result = {"download_speed": download_speed, "upload_speed": upload_speed, "ping": ping} # Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping
    print(result) # Affichage du résultat
     
def api_web_speedtest()->dict:
    """
        Calcule la vitesse de téléchargement, d'envoi et de ping.
        
        Returns:
            dict: Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping.
    """
    download_speed = get_download_speed() # Vitesse de téléchargement
    upload_speed = get_upload_speed() # Vitesse d'envoi
    ping = get_ping() # Ping
    result = {"download_speed": download_speed, "upload_speed": upload_speed, "ping": ping}    # Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping
    return result # Retourne le résultat

def cli_get_speedtest()->dict:
    """
        Calcule la vitesse de téléchargement, d'envoi et de ping.
        
        Returns:
            dict: Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping.
    """
    download_speed = get_download_speed() # Vitesse de téléchargement
    upload_speed = get_upload_speed() # Vitesse d'envoi
    ping = get_ping() # Ping
    return {"Débit Montant": f'{download_speed} Mb/s', "Débit Descendant": f'{upload_speed} Mb/s', "Ping": f'{ping} ms'} # Retourne le résultat

if __name__ == "__main__":
    api_speedtest()

