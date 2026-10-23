import socket

# 1. Crear un socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. puerto 5000
servidor.bind(("0.0.0.0", 5000))

# 5. Diccionario para registrar las mediciones
mediciones = {}

print("Servidor UDP iniciado. Esperando mediciones...")

try:
    # 7. Mantener el servidor en ejecución
    while True:

        # 3. Recibo datos del cliente
        data, direccion = servidor.recvfrom(1024)
        
        # 4. Decodifico el mensaje que me llega
        mensaje = data.decode("utf-8")

        # 6. Creo variables para mostrar el ip y puerto del cliente.
        ip_cliente = direccion[0]
        puerto_cliente = direccion[1]

        print(f"\nMensaje recibido de {ip_cliente}:{puerto_cliente}")
        print(f"Medición: {mensaje}")

        # 5. Registrar la medición en el diccionario
        mediciones[f"{ip_cliente}:{puerto_cliente}"] = mensaje

        # Mediciones registradas.
        print("Mediciones registradas:", mediciones)

except KeyboardInterrupt:
    print("\nServidor detenido por el usuario.")

finally:
    servidor.close()
    print("Socket UDP cerrado.")
