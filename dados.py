#!/usr/bin/python
import socket

print "interagindo com FTP SERVER"

ip = input("Digite o ip:")
porta = 21

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print banner

print "enviando usuario"
meusocket.send("USER ricardo\r\n")
banner = meusocket.recv(1024)
print banner

print "enviando senha"
meusocket.send("PASS ricardo\r\n")
banner = meusocket.recv(1024)
print banner

