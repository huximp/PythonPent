#!/usr/bin/python

import socket 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("172.16.1.108",21))

banner = tcp.recv(1024)
print banner

tcp.send("USER ftp\r\n")
user = tcp.recv(1024)
print user

tcp.send("PASS ftp\r\n")
pw = tcp.recv(1024)
print pw

tcp.send("HELP\r\n")
tcp.send("PWD\r\n")
cmd = tcp.recv(1024)
print cmd
