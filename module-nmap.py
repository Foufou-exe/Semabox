import nmap 

reponse = input(str("Enter the IP address: "))

def nmap_host_all(host):
    nm = nmap.PortScanner()
    nm.scan(host,'0-65535')
    if nm[host].state()== 'up':
        return nm[host]['tcp']

nmap_host_all(reponse)