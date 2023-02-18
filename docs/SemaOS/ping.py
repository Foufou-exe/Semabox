
import icmplib
import threading




def get_ping() -> int:
    """
        Envoie une requête ICMP et renvoie la durée du ping en millisecondes.
        
        Returns:
            int: Durée du ping en millisecondes.
            
        Raises:
            icmplib.exceptions.PingError: Si une erreur se produit lors de l'envoi de la requête ICMP.
    """
    while True: # Boucle infinie
        icmp = icmplib.ping("google.com", count=1) # Envoie une requête ICMP
        return int(icmp.avg_rtt)  # Retourne la durée du ping en millisecondes
        
def cli_ping():
    while True: # Boucle infinie
        icmp = icmplib.ping("google.com", count=1) # Envoie une requête ICMP
        return { "ping" : int(icmp.avg_rtt)} # Retourne la durée du ping en millisecondes
    
def api_ping():

    icmp = icmplib.ping("google.com", count=1) # Envoie une requête ICMP
    return { "ping" : int(icmp.avg_rtt)} # Retourne la durée du ping en millisecondes
        
        
if __name__ == "__main__":
    get_ping()