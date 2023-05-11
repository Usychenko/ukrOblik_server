import socket as s
import urllib.request
global_ip = urllib.request.urlopen("https://ident.me").read().decode('utf8')
hostname = s.gethostname()
ipAdress = s.gethostbyname(hostname)
print(str(ipAdress))
print(str(global_ip))
