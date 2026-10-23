import socket

# Crear el socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("172.31.116.85", 5001)

try:
    print("Conectado al servidor.")
    print("Escribe tus mensajes. Escribe 'salir' para terminar.\n")

    while True:
        # Leer mensaje desde el teclado
        mensaje = input("Cliente: ")

        # Se envia la variable mensaje al servidor.
        cliente.sendto(mensaje.encode(), addr)

        # Esperar respuesta del servidor
        data, direccion = cliente.recvfrom(1024)

        # Mostrar respuesta
        mensaje_recibido = data.decode()
        print(f"Servidor: {mensaje_recibido}\n")

        # Terminar si el usuario escribió salir
        if mensaje.lower() == "salir":
            print("Cliente desconectado.")
            break

finally:
    cliente.close()
