#!/usr/bin/env python3.11.1

# Importation des modules Python nécessaires
import sys
import uuid
import os
from .UID import semabox_uid

class Registres:
    def __init__(self):
        # Récupère le chemin absolu du fichier Python en cours d'exécution
        self.chemin_python = os.path.abspath(__file__)
        # Récupère le répertoire parent du fichier Python (qui est le répertoire de travail actuel)
        self.repertoire_travail = os.path.dirname(self.chemin_python)
    
    @staticmethod
    def generate_id():
        """
            Cette méthode génère un identifiant unique (UUID) et le retourne sous forme de chaîne de caractères.
        """
        return str(uuid.uuid4())

    @staticmethod 
    def lire_fichier():
        """
            Cette méthode lit le fichier "UID.txt" dans le dossier "UID.semabox_uid" et retourne son contenu.
        """
        return semabox_uid
   
        
    def check_variable(self):
        if semabox_uid == '':
            self.attribution_uid_variable()
            print("L'identifiant de la Semabox a été généré.")
        else:
            print("L'identifiant de la Semabox a déjà été généré : ", semabox_uid)
        
    def attribution_uid_variable(self, get_uid=None):
            """
                Cette méthode attribue l'identifiant contenu dans le fichier "" à la variable UID.semabox_uid.
            """
            if get_uid is None:
                get_uid = self.generate_id()

            if sys.platform == 'win32': # Windows
                file_path = os.path.join(self.repertoire_travail,"UID.py")
            else: # Linux ou autre
                file_path = os.path.join(self.repertoire_travail,"UID.py")
            
            # Ouverture du fichier en mode lecture
            with open(file_path, 'r') as f:
                # Lecture du contenu du fichier
                contenu = f.read()

            # Recherche de la ligne contenant la variable "UID.semabox_uid"
            nouvelle_valeur = get_uid
            lignes = contenu.split('\n')
            
            for i, ligne in enumerate(lignes):
                if ligne.startswith('UID.semabox_uid='):
                    # Modification de la valeur de la variable "UID.semabox_uid"
                    variable, ancienne_valeur = ligne.split('=')
                    lignes[i] = variable + "='" + nouvelle_valeur + "'"
                    break

            # Reconstruction du contenu modifié
            contenu = '\n'.join(lignes)

            # Ouverture du fichier en mode écriture pour écrire le contenu modifié
            with open(file_path, 'w') as f:
                f.write(contenu)
        
