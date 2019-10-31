import socket
import sys

#biblioteca par capturar hora e data
from calendar import*;
from time import*;

#Importando biblioteca de threads
from _thread import *

host = '' 
port = 8888

# cria socket para conexão
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket criado!")


try:						# Verifica se o socket está associado ao endereço local
	s.bind((host,port))
except socket.error:		# caso contrário, aborta!
	print("Bind falhou!")
	sys.exit()

print("Conexão criada!")

s.listen(10)				# permite até 10 clientes

print("Servidor está escutando...")

def clientthread(conn,addr):
	# enviando mensagem de boas vindas ao cliente qque se conectar
	welcome_message = ("Bem vindo ao servidor, cliente "  + str(addr[0]) + "\n")
	conn.send(welcome_message.encode())

	# enviando informações de data e hora aos clientes conectados
	time_message = asctime(localtime(time()))  
	conn.send(time_message.encode()) 

	# laço para conexão
	while True:
		try:						# enquanto receber dados sobre conexao
			data = conn.recv(1024)	# recebe mensagem de 'atualizou a hora'
			reply = "Cliente "+ str(addr[0]) +": "+ data.decode()
		except Exception as e:		# caso contrário, aborta!
			print("Bye bye, " + str(addr[0]) + "\n")
			break;
		print(reply)				# imprime mensagem de 'atualizou a hora'

		time_message = asctime(localtime(time()))	# Atualiza hora e data
		conn.sendall(time_message.encode()) 		# Inunda rede com infos atualizadas
	conn.close()

# laço que cria conexão com mais de 1 cliente, utilizando threads
while 1:	
	conn, addr = s.accept() 								# hand shake, pois nosso socket é tcp
	print("Conectado com "+ addr[0] + ":" + str(addr[1]))	# imprime informações da máqquina conectada
	start_new_thread(clientthread,(conn,addr))				# inicia conexão


s.close()






