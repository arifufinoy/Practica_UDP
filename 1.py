#Funciones importantes a trabajar:
    #socket() | bind() | sendto() para enviar | recvfrom() para recibir | close() para cerrar el socket.

import socket
import threading


#Trabajaremos con UDP
                    #Servidor IP               socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True: 
    server.bind(("localhost", 5000))
                        #Tamaño del datagrama
    data, addr = server.recvfrom(1024) #Regresa la data y el address de donde ha llegado.

    mensaje = data.decode()
    print(f"{mensaje} de {addr}")

    mensaje="Primero mensaje"
    server.sendto(mensaje.encode(),addr)
