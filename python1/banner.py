#!/usr/bin/python
import socket,sys

ip = sys.argv[1]

for porta in range(1,3386):
	meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	meusocket.connect((ip,porta))
	banner = meusocket.recv(1024)
	print banner

	if meusocket.connect_ex((ip,porta)) == 0:
		print "porta",porta,"[aberta]"
		meusocket.close()

