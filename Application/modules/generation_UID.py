import os
import uuid

def generate_id():
   id_semabox = str(uuid.uuid4())
   return id_semabox



def creation_dossier(id_semabox):
    # Créer un dossier nommé "mon_dossier"
    os.mkdir("SEMABOX_UID")

    # Créer un fichier texte nommé "mon_fichier.txt" dans le dossier "mon_dossier"
    with open("SEMABOX_UID/UID.txt", "w") as f:
        f.write(id_semabox)



def lire_fichier():
    with open("SEMABOX_UID/UID.txt", "r") as f:
        contenu = f.readline()
        return contenu


        
if __name__ == "__main__":
    creation_dossier(generate_id())