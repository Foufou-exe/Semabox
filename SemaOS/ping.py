
import icmplib
import time
import threading




def get_ping()->int:
    """
        Envoie une requête ICMP et renvoie la durée du ping en millisecondes.
        
        Returns:
            int: Durée du ping en millisecondes.
            
        Raises:
            icmplib.exceptions.PingError: Si une erreur se produit lors de l'envoi de la requête ICMP.
    """
    while True:
        icmp = icmplib.ping("google.com", count=1)
        return int(icmp.avg_rtt)

    
def api_get_ping()->dict:
    """
        Envoie une requête ICMP et renvoie la durée du ping en millisecondes.
            
        Returns:
            dict: Dictionnaire contenant la durée du ping en millisecondes.

            
        Raises:
            icmplib.exceptions.PingError: Si une erreur se produit lors de l'envoi de la requête ICMP.
    """
    while True:
        icmp = icmplib.ping("google.com", count=1)
        ping = int(icmp.avg_rtt)
        print({"ping": ping})
        time.sleep(10)
        
def run_api_get_ping():
    thread = threading.Thread(target=api_get_ping())
    thread.start()
        
if __name__ == "__main__":
    run_api_get_ping()