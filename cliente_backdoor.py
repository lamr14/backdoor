#!/usr/bin/env python
#_*_ coding: utf-8 _*_
#Las primeras dos líneas definen al intérprete y a la codificación
import socket #importa módulo de socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Agregamos un objeto del módulo socket. 
'''Vamos a crear una variable que se convertirá en ese objeto.'''
cliente.connect(('192.168.1.68', 7777)) #Recibe la tupla IP y puerto
cliente.close() #Cerramos el objeto con la función close.