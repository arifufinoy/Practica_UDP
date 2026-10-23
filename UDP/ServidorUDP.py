import threading
import socket
import json

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind(("0.0.0.0", 5000))
print("Esperando conexiones...")

datos = []

def tarea(data, direccion):

    #Mensaje a recibir.
    mensaje = json.loads(data.decode("utf-8"))

    match mensaje["opcion"]:

        case "1":
            usuario = {
                "cedula": mensaje["cedula"],
                "nombre": mensaje["nombre"],
                "correo": mensaje["correo"],
                "telefono": mensaje["telefono"],
                "preferencial": mensaje["preferencial"],
                "saldo": mensaje["saldo"]
            }

            datos.append(usuario)
            mensaje2 = "Usuario registrado correctamente"

            print(f"\nDatos del usuario")
            print(f"cedula: {mensaje["cedula"]}")
            print(f"nombre: {mensaje["nombre"]}")
            print(f"correo: {mensaje["correo"]}")
            print(f"telefono: {mensaje["telefono"]}")
            print(f"preferencial: {mensaje["preferencial"]}")
            print(f"saldo: {mensaje["saldo"]}")
            print(f"\n")

        case "2":
            cedula = mensaje["cedula"]
            mensaje2 = "Usuario no encontrado"

            for usuario in datos:
                if usuario["cedula"] == cedula:
                    mensaje2 = usuario
                    break
                
        case "3":
            cedula = mensaje["cedula"]
            monto = mensaje["monto"]
            mensaje2 = "Usuario no encontrado"

            for usuario in datos:
                if usuario["cedula"] == cedula:
                    usuario["saldo"] += monto
                    mensaje2 = "Saldo recargado correctamente"
                    break

        case _:
            mensaje2 = "Opcion no valida"


    #Mensaje que mandamos al cliente.
    socket_servidor.sendto(json.dumps(mensaje2).encode("utf-8"),direccion)


while True:
    data, direccion = socket_servidor.recvfrom(1024)
    hilo = threading.Thread(target=tarea, args=(data, direccion))
    hilo.start()