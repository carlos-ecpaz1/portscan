#!/usr/bin/python3
import socket,sys

for porta in range (1,65535):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if  meusocket.connect_ex((sys.argv[1],porta)) == 0:
        print ("Porta",porta, "[Aberta]")
        meusocket.close()
