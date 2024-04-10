#!/usr/bin/python

# port_scanner.py

import socket


print("Port Scanner by Mydas")
t_host = str(input("Target Host > "))
t_ip = socket.gethostbyname(t_host)

print(t_ip)

while 1:
    t_port = int(input("Port > "))
    
    try:
        sock = socket.socket()
        res = sock.connect((t_ip, t_port))
        print ("Port {}: Open" .format(t_port))
        sock.close()
    except:
        print ("Port {}: Close" .format(t_port))
print(">>>>>>>>>>> Scan Complete <<<<<<<<<<<")
