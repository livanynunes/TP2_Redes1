import socket
import sys
from calendar import*;
from time import*;

#Importando biblioteca de threads
from _thread import *

host = '' # ??
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket criado!")

try:
	s.bind((host,port))
except socket.error:
	print("Bind falhou!")
	sys.exit()

print("Conexão criada!")

s.listen(10)

print("Servidor está escutando...")

def clientthread(conn,addr):
	welcome_message = ("Bem vindo ao servidor, cliente "  + str(addr[0]) + "\n")
	conn.send(welcome_message.encode())

	time_message = asctime(localtime(time())) #teste 

	conn.send(time_message.encode()) #teste

	while True:
		data = conn.recv(1024)
		reply = "Cliente "+ str(addr[0]) +": "+ data.decode()
		if not data:
			print("Bye bye, " + str(addr[0]) + "\n")
			break;
		print(reply)
		time_message = asctime(localtime(time()))
		conn.sendall(time_message.encode()) #inunda rede
	conn.close()

#######################

while 1:
	conn, addr = s.accept()
	print("Conectado com "+ addr[0] + ":" + str(addr[1]))
	start_new_thread(clientthread,(conn,addr))


s.close()






