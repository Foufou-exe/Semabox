import subprocess
import sys



def get_latency() -> str:
    """
        Description:
            Cette fonction récupère la latence en effectuant un ping sur google.com
            
        Returns:
            str: Latence en ms
    """    # Déterminer la plateforme d'exécution
    platform = "linux" if "linux" in sys.platform else "windows"
    # Effectuer un ping
    while True:
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        try:
            if platform == "linux":
                latency = result.split("=")[1]
            else:
                latency = result.split("=")[1]
        except IndexError:
            latency = None
        return latency


def api_get_latence():
    """
        Description:
            Cette fonction effectue un ping sur google.com et retourne la latence dans un dictionnaire
            
        Returns:
            dict: {"latency": latence en ms}
    """
    
    ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
    # Récupérer la latence
    result = ping.stdout.split()[15]
    return { "latency": result.split("=")[1]}

    
if __name__ == "__main__":
   api_get_latence()