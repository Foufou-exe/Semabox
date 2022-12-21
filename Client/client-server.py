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
output = exec(request)

# Récupération des résultats du script exécuté
results = output

# Booléen pour suivre si le fichier a déjà été envoyé
file_sent = False

while True:
    # Réception de la requête du client
    request = connection.recv(1024)

    if not file_sent:
        # Envoi du fichier au client
        with open('file.txt', 'rb') as f:
            connection.send(f.read())
        file_sent = True
    else:

    # Envoi des résultats au client
    connection.send(results)

    # Fermeture de la connexion
    connection.close()