import socket
import random
import time
import json

# 1 y 2. Crear un socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = ("172.31.116.85", 5000)

#ESTA ES UN DICCIONARIO
sensores= {
    "S1" : ["Temperatura", 30],
    "S2" : ["Humedad", 80],
    "S3" : ["Distancia", 20],
    "S4" : ["Nivel agua", "Medio"]
}

try:
    while True:
        #Mediciones randomicas
        medicion = round(random.uniform(20.0, 35.0), 2)

        for codigo, datos in sensores.items():
            #Diccionario para mandar.
            mensaje = {
                "codigo": codigo,
                "sensor": datos[0],
                "valor": datos[1]
            }
            #Envio el mensaje
            cliente.sendto(json.dumps(mensaje).encode("utf-8"), servidor)
            #Imprimo mensaje dentro de mi terminal.
            print(f"{mensaje}")
            #Enviar datos mediante UDP
            time.sleep(1)
            

except KeyboardInterrupt:
    print("\nTransmision del sensor finalizada.")

cliente.close()