import uuid
import socket

"""
    Creation des fonctions
"""


# get the hostname of the client
def _get_hostname():
    global hostname, dnsname
    hostname = socket.gethostbyname(socket.gethostname())
    dnsname = socket.getfqdn(hostname)


list_of_uid = [dnsname, my_uid]






"""
    Appelle des fonctions
"""
_generate_uid()
_get_hostname()