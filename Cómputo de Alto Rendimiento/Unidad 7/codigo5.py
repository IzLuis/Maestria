import threading
import time
import random

N = 5  # Número de filósofos (y palillos)

# Cada palillo es un Lock entre filósofos
palillos = [threading.Lock() for _ in range(N)]

# Cola de espera para comer (FIFO)
cola = []

# Lock para acceder a la cola de forma segura
lock_cola = threading.Lock()

# Semáforo que permite solo 2 filósofos comiendo simultáneamente
permiso_para_comer = threading.Semaphore(2)

def filosofo(i):
    while True:
        # Paso 1: Se agrega a la cola de espera
        with lock_cola:
            cola.append(i)
            print(f"Filósofo {i} se unió a la cola: {cola}")

        # Paso 2: Espera a que sea su turno Y haya permiso para comer
        while True:
            with lock_cola:
                es_mi_turno = (cola[0] == i)  # Verifica si está al frente

            # Si es su turno y hay permiso, avanza
            if es_mi_turno and permiso_para_comer.acquire(blocking=False):
                break
            time.sleep(0.1)  # Espera antes de volver a revisar

        # Paso 3: Toma los dos palillos
        palillos[i].acquire()
        palillos[(i + 1) % N].acquire()

        print(f"Filósofo {i} está comiendo...")
        time.sleep(random.uniform(1, 2))  # Simula tiempo comiendo

        # Paso 4: Libera palillos y permiso
        palillos[i].release()
        palillos[(i + 1) % N].release()
        permiso_para_comer.release()

        # Paso 5: Sale de la cola
        with lock_cola:
            print(f"Filósofo {i} terminó de comer.")
            cola.pop(0)

# Crear e iniciar los hilos
for i in range(N):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

# Para evitar que el programa termine de inmediato
while True:
    time.sleep(1)
