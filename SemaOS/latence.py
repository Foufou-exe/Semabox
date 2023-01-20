import subprocess
import time
import threading



def get_latency()->str:
    """
        Description:
            Cette fonction récupère la latence en effectuant un ping sur google.com
            
        Returns:
            str: Latence en ms
    """
    while True:
        # Effectuer un ping
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        return result.split("=")[1]
        


def cli_latence():
    """
        Description:
            Cette fonction effectue un ping sur google.com et retourne la latence dans un dictionnaire
            
        Returns:
            dict: {"latency": latence en ms}
    """
    while True:
        # Effectuer un ping
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        return { "latency": result.split("=")[1]}

def run_cli_latency():
    """
        Description:
            Cette fonction lance un thread qui appelle la fonction cli_latency en boucle
    """
    thread = threading.Thread(target=cli_latence())
    thread.start()

    
if __name__ == "__main__":
    run_cli_latency()