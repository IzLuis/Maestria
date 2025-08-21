import threading  # Importa la biblioteca para trabajar con hilos

# Crea un objeto Lock para sincronizar el acceso a recursos compartidos
lock = threading.Lock()

# Variable compartida entre los hilos
shared_counter = 0

# Función que incrementa el contador compartido
def increment():
    global shared_counter  # Declara que se usará la variable global
    for _ in range(100000):  # Realiza 100,000 incrementos
        with lock:  # Adquiere el lock para garantizar exclusión mutua
            shared_counter += 1  # Incrementa el contador de forma segura

# Crea una lista de 10 hilos, cada uno ejecutando la función increment
threads = [threading.Thread(target=increment) for _ in range(10)]

# Inicia todos los hilos
[t.start() for t in threads]

# Espera a que todos los hilos terminen
[t.join() for t in threads]

# Imprime el resultado final del contador compartido
print(f"Resultado final: {shared_counter}")
