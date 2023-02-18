#!/usr/bin/env python3.11.1

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
        Cette fonction crée un dossier nommé "Semabox_UID" et y crée un fichier texte nommé "UID.txt" contenant l'identifiant
        passé en paramètre.
        
        Paramètres :
            - id_semabox (str) : identifiant à écrire dans le fichier "UID.txt".
    """

    if os.name == 'nt': # Windows
        file_path = os.path.join("SemaOS", "Semabox_UID") # Création du dossier "Semabox_UID"
    else: # Linux ou autre
        file_path = os.path.join("../Semabox/SemaOS", "Semabox_UID") # Création du dossier "Semabox_UID"
    # Création du dossier "Semabox_UID"
    os.mkdir(file_path) # Création du dossier "Semabox_UID"

    # Utiliser os.path.join pour construire le chemin absolu
    file_other = os.path.join(file_path,"UID.txt") 
    # Création du fichier "UID.txt" dans le dossier "Semabox_UID" et écriture de l'identifiant dedans
    with open(file_other, "w") as f: # Ouverture du fichier "UID.txt" en écriture
        f.write(id_semabox) # Ecriture de l'identifiant dans le fichier "UID.txt"

def lire_fichier():
    """
        Cette fonction lit le fichier "UID.txt" dans le dossier "Semabox_UID" et retourne son contenu.
    """
    # Condition pour vérifier si le système d'exploitation est Windows ou Linux
    if os.name == 'nt': # Windows
        file_path = os.path.join("SemaOS", "Semabox_UID","UID.txt") # Chemin absolu du fichier "UID.txt"
    else: # Linux ou autre
        file_path = os.path.join("../Semabox/SemaOS", "Semabox_UID","UID.txt") # Chemin absolu du fichier "UID.txt"
        
    with open(file_path, "r") as f: # Ouverture du fichier "UID.txt" en lecture
        return f.readline() # Lecture du fichier "UID.txt" et retour de son contenu
    
def check_file():
    """
        Cette fonction vérifie si le fichier "UID.txt" existe dans le dossier "Semabox_UID".
        Si le fichier n'existe pas, on appelle la fonction creation_dossier() avec un identifiant généré par generate_id().
        Sinon, on appelle la fonction lire_fichier().
    """
    # Condition pour vérifier si le système d'exploitation est Windows ou Linux
    if os.name == 'nt': # Windows
        file_path = os.path.join("SemaOS/Semabox_UID") # Chemin absolu du fichier "UID.txt"
    else: # Linux ou autre
        file_path = os.path.join("../Semabox/SemaOS/Semabox_UID") # Chemin absolu du fichier "UID.txt"
        
    if not os.path.exists(file_path): # Si le fichier "UID.txt" n'existe pas
        creation_dossier(generate_id()) # Appel de la fonction creation_dossier() avec un identifiant généré par generate_id()
    else: # Si le fichier "UID.txt" existe
        print(lire_fichier()) # Appel de la fonction lire_fichier()
        
# Si ce fichier est exécuté directement, on appelle la fonction creation_dossier() avec un identifiant généré par generate_id()
if __name__ == "__main__":
    check_file()