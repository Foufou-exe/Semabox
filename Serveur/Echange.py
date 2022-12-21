import socket

# Création du client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client.connect(('localhost', 8000))

# Envoi de la requête au serveur
client.send(b'Execute script.py')

# Réception des résultats du serveur
results = client.recv(1024)
print(results)

# Fermeture de la connexion
client.close()