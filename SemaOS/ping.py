
import icmplib
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

    
        
def cli_ping():
    while True:
        icmp = icmplib.ping("google.com", count=1)
        return { "ping" : int(icmp.avg_rtt)}
    
def api_ping():

    icmp = icmplib.ping("google.com", count=1)
    return { "ping" : int(icmp.avg_rtt)}
        
        
if __name__ == "__main__":
    get_ping()