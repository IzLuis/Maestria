import socket
import threading

# Función para recibir mensajes del cliente
def recibir_mensajes(conexion):
    while True:
        try:
            mensaje = conexion.recv(1024).decode('utf-8')  # Recibe hasta 1024 bytes y decodifica
            if mensaje.lower() == "bye":                  # Si el cliente dice "bye", termina el chat
                print("El cliente terminó la conversación.")
                break
            print(f"Cliente: {mensaje}")                  # Muestra el mensaje recibido
        except:
            break  # Si ocurre un error (por ejemplo, desconexión), termina
    conexion.close()

# Función para enviar mensajes al cliente
def enviar_mensajes(conexion):
    while True:
        mensaje = input("Tú: ")                           # Pide entrada del servidor
        conexion.send(mensaje.encode('utf-8'))            # Envía el mensaje codificado
        if mensaje.lower() == "bye":                      # Si se escribe "bye", se termina el chat
            break
    conexion.close()

# Función principal
def main():
    puerto = 4545
    # Crea el socket del servidor
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mi_socket.bind(("127.0.0.1", puerto))        # Lo vincula a la IP local y puerto 4545
    mi_socket.listen(1)                                   # Escucha una conexión entrante

    print("Servidor esperando conexión...")
    conexion, direccion = mi_socket.accept()              # Acepta conexión del cliente
    print(f"Cliente conectado desde {direccion}")

    # Crea dos hilos: uno para recibir y otro para enviar mensajes
    hilo_receptor = threading.Thread(target=recibir_mensajes, args=(conexion,))
    hilo_emisor = threading.Thread(target=enviar_mensajes, args=(conexion,))

    # Inicia los hilos
    hilo_receptor.start()
    hilo_emisor.start()

    # Espera a que ambos hilos terminen
    hilo_receptor.join()
    hilo_emisor.join()
    mi_socket.close()
    print("Chat finalizado.")

# Ejecuta la función principal
if __name__ == "__main__":
    main()
