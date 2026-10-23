import threading
import socket

# Crear el socket UDP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Escuchar en todas las interfaces de red, puerto 5001
socket_servidor.bind(("0.0.0.0", 5001))

print("Servidor iniciado. Esperando mensajes...")


def tarea(data, direccion):
    mensaje = data.decode()
    print(f"Mensaje recibido de {direccion}: {mensaje}")

    # Comprobar si el cliente desea salir
    if mensaje.lower() == "salir":
        respuesta = "Conexion finalizada por el cliente"
    else:
        respuesta = "Hola, soy el servidor. Mensaje recibido."

    socket_servidor.sendto(respuesta.encode(), direccion)

try:
    while True:
        data, direccion = socket_servidor.recvfrom(1024)

        hilo = threading.Thread(
            target=tarea,
            args=(data, direccion)
        )
        hilo.start()

except KeyboardInterrupt:
    print("\nServidor cerrado.")

finally:
    socket_servidor.close()
