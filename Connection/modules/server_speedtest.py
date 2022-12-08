import pyspeedtest

def Speed_test():
    global ping, download, upload
    t = pyspeedtest.SpeedTest("google.com")
    resultat_ping = t.ping()
    resultat_download = t.download()
    resultat_upload = t.upload()
    ping = int(resultat_ping)
    download = "{0:.2f}".format(resultat_download / 1000000 * 8)
    upload = "{0:.2f}".format(resultat_upload / 1000000 * 8)

Speed_test()
