import socket
import sys
from calendar import*;
from time import*;

#Importando biblioteca de threads
from _thread import *

host = '192.168.0.105' ## mudar pro host da maquina do cliente
port = 8888

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((host,port))
welcome_message = c.recv(1024)
print(welcome_message.decode())

while True:

	time_recv = c.recv(1024)
	print('As infos de data e hora : ' + time_recv.decode())

	continuar = input('Deseja continuar [y/n]? : ')
	if continuar =='y' || continuar == '':
		c.send("Atualizou a hora!".encode());
		continue
	else :
		break

#fechar conexao
c.close()