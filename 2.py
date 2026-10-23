
import socket

# Crear el socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dirección IP y puerto del servidor
addr = ("172.31.116.85", 5001)

try:
    # Enviar mensaje al servidor
    mensaje = "Primer mensaje cliente"
    cliente.sendto(mensaje.encode(), addr)

    # Recibir respuesta del servidor
    data, addr = cliente.recvfrom(1024)

    # Decodificar e imprimir el mensaje recibido
    mensaje_recibido = data.decode()
    print(f"Respuesta del servidor: {mensaje_recibido}")

finally:
    # Cerrar el socket
    cliente.close()
