import os
import uuid

def generate_id():
   global id_semabox
   id_semabox = str(uuid.uuid4())
   return id_semabox



def creation_dossier(id_semabox):
    # Créer un dossier nommé "mon_dossier"
    os.mkdir("SEMABOX_UID")

    # Créer un fichier texte nommé "mon_fichier.txt" dans le dossier "mon_dossier"
    with open("SEMABOX_UID/UID.txt", "w") as f:
        f.write(id_semabox)



def lire_fichier():
    global contenu_lu
    with open("SEMABOX_UID/UID.txt", "r") as f:
        contenu = f.readline()
        contenu_lu = contenu
        return contenu_lu



        
if __name__ == "__main__":
    creation_dossier(generate_id())