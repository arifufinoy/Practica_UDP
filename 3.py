import threading
import socket
import json

socket_servidor=socket. socket(socket.AF_INET, socket. SOCK_DGRAM)
socket_servidor.bind(("0.0.0.0",5000))
print("Esperando conexiones...")

def tarea(data, direccion):

    #Mensaje a recibir.
    mensaje=json.loads(data.decode("utf-8"))
    print(f"Direccion Cliente: {direccion}")
    print(f"Cdigo: {mensaje["codigo"]}")
    print(f"Sensor: {mensaje["sensor"]}")
    print(f"Valor: {mensaje["valor"]}")
    print(f"\n------------------")

    #Mensaje a mandar al cliente.
    mensaje2="Datos recibidos."
    socket_servidor. sendto(mensaje2.encode(),direccion)

while True:
    data, direccion = socket_servidor.recvfrom(1024)
    hilo = threading. Thread(target=tarea, args=(data, direccion))
    hilo.start()