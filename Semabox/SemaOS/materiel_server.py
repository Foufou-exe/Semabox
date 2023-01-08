"""
    Description: Ce module contient des fonctions qui permettent de récupérer des informations sur le serveur exécutant le script.

    Importation des modules Python nécessaires:
        psutil - Ce module permet de récupérer des informations sur le système, notamment sur les ressources utilisées (CPU, RAM, disques, etc.).
        platform - Ce module permet de récupérer des informations sur le système d'exploitation du serveur (nom, version, etc.).

    Fonctions:
        get_server_info() - Cette fonction retourne un dictionnaire contenant des informations sur le serveur exécutant le script. 
        Les informations incluent le nombre de coeurs CPU, l'utilisation CPU, la quantité de mémoire RAM, le nombre de disques, le temps écoulé depuis l'allumage et le nom de l'OS.
"""
# Importation des modules Python nécessaires
import psutil
import platform

# Définition des fonctions
def get_server_info():
    """
        Description:
            Cette fonction retourne un dictionnaire contenant des informations sur le serveur exécutant le script. Les informations incluent le nombre de coeurs CPU, l'utilisation CPU, la quantité de mémoire RAM, le nombre de disques, le temps écoulé depuis l'allumage et le nom de l'OS.
        
        Returns:
            dict: Un dictionnaire contenant les informations sur le serveur.
    """
    
    # Récupération de l'utilisation CPU
    cpu_utilization = psutil.cpu_percent()

    # Récupération du nombre de coeurs CPU
    num_cpus = psutil.cpu_count()

    # Récupération de la quantité de mémoire RAM
    memory = psutil.virtual_memory() 
    ram_size = "{0:.2f}".format(memory.total / (1024 ** 3))

    # Récupération du nombre de disques
    num_disks = len(psutil.disk_partitions())

    # Récupération du nom de l'OS
    os_name = platform.system()

    # Récupération du temps écoulé depuis l'allumage
    uptime = psutil.boot_time()

    # Conversion du temps écoulé en heures
    uptime_hours = int(uptime / 3600)

    # Retour du dictionnaire
    return {
        'num_cpus': num_cpus,
        'cpu_utilization': cpu_utilization,
        'ram_size_go': ram_size,
        'num_disks': num_disks,
        'uptime_hours': uptime_hours,
        'os_name': os_name
    }


if __name__ == '__main__':
    # Affichage des informations du serveur
    get_server_info()