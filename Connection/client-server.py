import uuid
import socket

"""
    Creation des fonctions
"""

# generate a unique id for the client
def _generate_uid():
    global my_uid
    my_uid = str(uuid.uuid4())

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