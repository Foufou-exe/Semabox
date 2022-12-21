import time
import requests
import icmplib



def get_download():
  # Choisissez un fichier de test de grande taille pour mesurer la vitesse de téléchargement
  test_file_url = "http://ipv4.download.thinkbroadband.com/50MB.zip"
  # Enregistrez le temps de départ
  start_time = time.time()
  # Téléchargez le fichier de test
  r = requests.get(test_file_url)
  # Enregistrez le temps de fin
  end_time = time.time()
  # Calculez la durée du téléchargement en secondes
  elapsed_time = end_time - start_time
  # Calculez la vitesse de téléchargement en octets par seconde
  download_speed = len(r.content) / elapsed_time
  
  return "{0:.2f}".format(download_speed / 1000000)



def get_upload_speed():
  # URL de téléchargement
  url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"

  # Chemin d'accès au fichier à envoyer
  file_path = "Connection\modules\download\TESTMB.zip"
  
  # Ouvrez le fichier en mode binaire
  with open(file_path, 'rb') as file:
    # Enregistrez le temps de départ
    depart_time = time.time()

    # Envoyez le fichier à l'aide de la méthode POST de requests
    files = {'file': file}
    response = requests.post(url, files=files)

    # Enregistrez le temps de fin
    end_time = time.time()

  # Calculate the upload speed
  upload_speed = len(response.content) / (end_time - depart_time)
  
  return "{0:.2f}".format(upload_speed)
  


def get_ping():
  # Créez un objet ICMP
  icmp = icmplib.ping("ipv4.download.thinkbroadband.com", count=1)
  # Envoyez une requête ICMP et attendez la réponse
  # Affichez la durée du ping
  ping = int(icmp.avg_rtt)
  return ping
  
