import socket
import threading

# Función para recibir mensajes del servidor
def recibir_mensajes(socket_cliente):
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode('utf-8')  # Recibe y decodifica mensaje
            if mensaje.lower() == "bye":                         # Si recibe "bye", termina el chat
                print("El servidor terminó la conversación.")
                break
            print(f"Servidor: {mensaje}")                         # Muestra mensaje recibido
        except:
            break
    socket_cliente.close()

# Función para enviar mensajes al servidor
def enviar_mensajes(socket_cliente):
    while True:
        mensaje = input("Tú: ")                                   # Captura mensaje desde terminal
        socket_cliente.send(mensaje.encode('utf-8'))              # Lo envía al servidor
        if mensaje.lower() == "bye":                              # Si escribes "bye", termina el chat
            break
    socket_cliente.close()

# Función principal
def main():
    host = "127.0.0.1"  # Usa el nombre del host local
    puerto = 4545                # Mismo puerto que el servidor

    # Crea el socket del cliente
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((host, puerto))                        # Conecta al servidor

    print("Conectado al servidor. Puedes comenzar a chatear.")

    # Crea dos hilos: uno para recibir, otro para enviar
    hilo_receptor = threading.Thread(target=recibir_mensajes, args=(socket_cliente,))
    hilo_emisor = threading.Thread(target=enviar_mensajes, args=(socket_cliente,))

    # Inicia ambos hilos
    hilo_receptor.start()
    hilo_emisor.start()

    # Espera a que ambos terminen
    hilo_receptor.join()
    hilo_emisor.join()
    print("Chat finalizado.")

# Ejecuta el cliente si se llama directamente
if __name__ == "__main__":
    main()
