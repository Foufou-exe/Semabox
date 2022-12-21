import socket
from modules.info_server import get_ip_address as ip

# Création du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse et un port
server.bind((ip, 8000))

# Écoute des connexions entrantes
server.listen()

# Acceptation d'une connexion
connection, address = server.accept()

# Réception de la requête du client
request = connection.recv(1024)

# Exécution du script spécifié dans la requête
exec(request)

# Récupération des résultats du script exécuté
results = 'Script executed successfully'

# Envoi des résultats au client
connection.send(results)

# Fermeture de la connexion
connection.close()