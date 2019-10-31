import socket
import sys

#biblioteca par capturar hora e data
from calendar import*;
from time import*;

# biblioteca para utilizar função de controle de tempo
import time 

#Importando biblioteca de threads
from _thread import *

port = 8888
host = '192.168.0.101' 		# host da maquina do cliente
#host = '192.168.1.30' 		# muda de acordo com o cliente,
							# para saber, usar 'ipconfig' 

# cria socket para conexão
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host,port))

welcome_message = c.recv(1024)	# recebendo mensagem de boas vindas do servidor
print(welcome_message.decode())	# imprimeindo mensagem de boas vindas

# laço de conexão, para sair digite Ctrl-C
while True:	

	# recebendo data e hora do servidor, e imprimindo
	time_recv = c.recv(1024)	
	print('As infos de data e hora : ' + time_recv.decode())

	# envia mensagem ao servidor que hora do cliente foi atualizada!
	# serve para confirmar que o cliente ainda está conectado
	c.send("Atualizou a hora!".encode());

	# atualiza o horário a cada X segundos, para testes bom deixar 5seg 
	time.sleep(5) # para o exercicio utilizamos 60segundos
	
#fechando conexao
c.close()