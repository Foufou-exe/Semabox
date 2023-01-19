import subprocess
import time
import threading



def get_latency()->str:
    while True:
        # Effectuer un ping
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        return result.split("=")[1]
        


def cli_latence():
    while True:
        # Effectuer un ping
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        return { "latency": result.split("=")[1]}

def run_cli_latency():
    thread = threading.Thread(target=cli_latence())
    thread.start()

    
if __name__ == "__main__":
    run_cli_latency()