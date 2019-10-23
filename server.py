import socket
import sys

#Importando biblioteca de threads
from _thread import *

host = '' # ??
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket created")

try:
	s.bind((host,port))
except socket.error:
	print("bind failed")
	sys.exit()

print("Sock has been bounded")

s.listen(10)

print("Sock is ready")

def clientthread(conn):
	welcome_message = "Welcome to the server. Type something and hit enter\n"
	conn.send(welcome_message.encode())

	while True:
		data = conn.recv(1024)
		reply = "Ok "+ data.decode()
		if not data:
			break;
		print(reply)
		conn.sendall(data)
	conn.close()

#######################3



while 1:
	conn, addr = s.accept()
	print("Conectado com "+ addr[0] + ":" + str(addr[1]))
	start_new_thread(clientthread,(conn,))


s.close()






