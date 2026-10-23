
import socket
import json

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP del equipo donde se ejecuta el servidor
servidor = ("172.31.116.84", 5000)

# Evitar que el cliente espere indefinidamente
cliente.settimeout(5)

while True:

    print("\n--- MENU ---")
    print("1. Registrar")
    print("2. Consultar")
    print("3. Recargar")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("\nIngrese los datos del usuario")

        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        telefono = input("Telefono: ")
        preferencial = input("Preferencial (si/no): ").lower()
        saldo = float(input("Saldo inicial: "))

        mensaje = {
            "opcion": opcion,
            "cedula": cedula,
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "preferencial": preferencial,
            "saldo": saldo
        }

    elif opcion == "2":
        cedula = input("Cedula del usuario a consultar: ")

        mensaje = {
            "opcion": opcion,
            "cedula": cedula
        }

    elif opcion == "3":
        cedula = input("Cedula del usuario: ")
        monto = float(input("Monto a recargar: "))

        mensaje = {
            "opcion": opcion,
            "cedula": cedula,
            "monto": monto
        }

    elif opcion == "4":
        print("Cerrando cliente...")
        break

    else:
        print("Opcion no valida")
        continue

    try:
        #Enviar mensaje al servidor-
        datos = json.dumps(mensaje).encode("utf-8")
        cliente.sendto(datos, servidor)

        print("\nMensaje enviado:", mensaje)

        #Recibir respuesta del servidor-
        data, direccion = cliente.recvfrom(1024)
        respuesta = json.loads(data.decode("utf-8"))

        print("Respuesta del servidor:", respuesta)

    except json.JSONDecodeError:
        print("Error")

cliente.close()
