import threading
import socket

# Fonction pour obtenir le nom du service associé à un port donné
def get_service_name(port):
  try:
    # Utiliser la fonction getservbyport de la bibliothèque socket pour obtenir le nom du service
    return socket.getservbyport(port)
  except OSError:
    # Si le port n'a pas de service associé, retourner "unknown"
    return "inconu"

def scan_port(port):
  # Créer un socket pour se connecter au port
  s = socket.socket()
  try:
    # Tenter de se connecter au port
    s.connect(("10.60.56.36", port))
  except OSError:
    # Si la connexion échoue, passer au prochain port
    return
  else:
    # Si la connexion réussie, le port est ouvert
    service_name = get_service_name(port)
    print(f"PORT: {port}/tcp | OPEN✅ | SERVICE: {service_name}")
  finally:
    # Fermer le socket
    s.close()

# Parcourir tous les ports de 1 à 65535
ports = range(1, 65535)
# Créer une liste de threads pour les scans
threads = [threading.Thread(target=scan_port, args=(port,)) for port in ports]
# Démarrer tous les threads
for thread in threads:
  thread.start()