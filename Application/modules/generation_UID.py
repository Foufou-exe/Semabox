# Importation des modules Python nécessaires
import os
import uuid

def generate_id():
    """
        Cette fonction génère un identifiant unique (UUID) et le retourne sous forme de chaîne de caractères.
    """
    return str(uuid.uuid4())


def creation_dossier(id_semabox):
    """
        Cette fonction crée un dossier nommé "SEMABOX_UID" et y crée un fichier texte nommé "UID.txt" contenant l'identifiant
        passé en paramètre.
        
        Paramètres :
            - id_semabox (str) : identifiant à écrire dans le fichier "UID.txt".
    """
    # Création du dossier "SEMABOX_UID"
    os.mkdir("SEMABOX_UID")

    # Création du fichier "UID.txt" dans le dossier "SEMABOX_UID" et écriture de l'identifiant dedans
    with open("SEMABOX_UID/UID.txt", "w") as f:
        f.write(id_semabox)

def lire_fichier():
    """
        Cette fonction lit le fichier "UID.txt" dans le dossier "SEMABOX_UID" et retourne son contenu.
    """
    with open("SEMABOX_UID/UID.txt", "r") as f:
        return f.readline()

# Si ce fichier est exécuté directement, on appelle la fonction creation_dossier() avec un identifiant généré par generate_id()
if __name__ == "__main__":
    creation_dossier(generate_id())
