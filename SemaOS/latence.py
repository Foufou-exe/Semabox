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
        
    
def api_get_latency()->dict:
    while True:
        # Effectuer un ping
        ping = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        # Récupérer la latence
        result = ping.stdout.split()[15]
        latency = { "lantency": result.split("=")[1]}
        print(latency)
        time.sleep(1)
        
def run_api_get_latency():
    thread = threading.Thread(target=api_get_latency())
    thread.start()


    
if __name__ == "__main__":
    run_api_get_latency()  