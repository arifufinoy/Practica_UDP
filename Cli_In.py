import socket
import random
import time
import json

# 1 y 2. Crear un socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = ("172.31.116.85", 5000)

#ESTA ES UN DICCIONARIO
sensores= {
    "S1" : ["Temperatura", 30°],
    "S2" : ["Humedad", 80],
    "S3" : ["Distancia", 20]
    "S4" : ["Nivel agua", "Medio"]
}

try:
    while True:
        #Mediciones randomicas
        medicion = round(random.uniform(20.0, 35.0), 2)

        #Lo que se muestra en el serivdor
        mensaje = f"Codigo: {codigo}, Sensor: {sensor}, Medicion: {medicion} °C"

        #Enviar datos mediante UDP
        cliente.sendto(mensaje.encode("utf-8"), servidor)

        #Lo que se muestra en mi terminal
        print(f"El sensor {sensor} ({codigo}) transmitió: {medicion} °C")

        #3 Segundo antes de enviar otra pedicion
        time.sleep(3)

finally:
    cliente.close()


'''
import socket
import random
import time
import json

# 1 y 2. Crear un socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = ("172.31.116.85", 5000)

#ESTA ES UN DICCIONARIO
sensores= {
    "S1" : ["Temperatura", 30°],
    "S2" : ["Humedad", 80],
    "S3" : ["Distancia", 20]
    "S4" : ["Nivel agua", "Medio"]
}

try:
    while True:
        #Mediciones randomicas
        medicion = round(random.uniform(20.0, 35.0), 2)

        for i in range sensores.items():
            mensaje = i
            print(f"{mensaje}")
            #Enviar datos mediante UDP
            time.sleep(3)
            cliente.sendto(json.dumps(mensaje.encode("utf-8"), servidor))

        #Lo que se muestra en mi terminal
        print(f"El sensor {sensor} ({codigo}) transmitió: {medicion} °C")

        #3 Segundo antes de enviar otra pedicion
        time.sleep(3)

except KeyboardInterrupt:
    print("\Transmision del sensor finalizada.")

finally:
    cliente.close()
'''