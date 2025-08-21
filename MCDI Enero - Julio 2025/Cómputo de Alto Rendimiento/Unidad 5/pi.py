from mpi4py import MPI
import numpy as np
import time

def calcular_pi(n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # El proceso 0 pide el número de subdivisiones
    if rank == 0:
        n = int(input("Ingrese el número de subdivisiones: "))
    else:
        n = None
    
    # Se transmite el valor de n a todos los procesos
    n = comm.bcast(n, root=0)
    
    # Medición del tiempo de inicio en paralelo
    comm.Barrier()
    start_time = MPI.Wtime()
    
    # Definir la suma de Riemann
    h = 1.0 / n  # Ancho de cada subintervalo
    local_sum = 0.0
    for i in range(rank, n, size):
        x = (i + 0.5) * h
        local_sum += 4.0 / (1.0 + x * x)
    local_sum *= h
    
    # Reducir los resultados parciales al proceso 0
    pi_total = comm.reduce(local_sum, op=MPI.SUM, root=0)
    
    # Medición del tiempo de finalización en paralelo
    comm.Barrier()
    end_time = MPI.Wtime()
    elapsed_time = end_time - start_time
    
    # Medición de tiempo en versión secuencial (solo en el proceso 0)
    if rank == 0:
        start_seq = time.time()
        pi_seq = sum(4.0 / (1.0 + ((i + 0.5) * h) ** 2) for i in range(n)) * h
        end_seq = time.time()
        elapsed_seq = end_seq - start_seq
        
        print(f"Aproximación de π con {n} subdivisiones: {pi_total}")
        print(f"Tiempo transcurrido (paralelo): {elapsed_time:.6f} segundos")
        print(f"Tiempo transcurrido (secuencial): {elapsed_seq:.6f} segundos")
        
        # Cálculo del Speed-up y eficiencia
        speed_up = elapsed_seq / elapsed_time
        efficiency = speed_up / size
        print(f"Speed-up: {speed_up:.2f}")
        print(f"Eficiencia: {efficiency:.2f}")

if __name__ == "__main__":
    calcular_pi(0)
