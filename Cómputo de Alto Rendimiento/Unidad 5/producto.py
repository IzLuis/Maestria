from mpi4py import MPI
import numpy as np
import time

def producto_escalar():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    N = 10 # Tamaño del vector
    
    if rank == 0:
        A = np.random.rand(N)
        B = np.random.rand(N)
    else:
        A = None
        B = None
    
    # Tamaño del fragmento que recibe cada proceso
    local_N = N // size
    local_A = np.zeros(local_N)
    local_B = np.zeros(local_N)
    
    # Distribuir los vectores entre los procesos
    comm.Scatter(A, local_A, root=0)
    comm.Scatter(B, local_B, root=0)
    
    # Medición del tiempo en paralelo
    comm.Barrier()
    start_time = MPI.Wtime()
    
    # Producto escalar parcial
    local_dot = np.dot(local_A, local_B)
    
    # Reunir resultados en el proceso 0
    total_dot = comm.reduce(local_dot, op=MPI.SUM, root=0)
    
    comm.Barrier()
    end_time = MPI.Wtime()
    elapsed_time = end_time - start_time
    
    if rank == 0:
        # Versión secuencial
        start_seq = time.time()
        dot_seq = np.dot(A, B)
        end_seq = time.time()
        elapsed_seq = end_seq - start_seq
        
        print(f"Producto escalar paralelo: {total_dot}")
        print(f"Producto escalar secuencial: {dot_seq}")
        print(f"Tiempo transcurrido (paralelo): {elapsed_time:.6f} segundos")
        print(f"Tiempo transcurrido (secuencial): {elapsed_seq:.6f} segundos")
        
        # Cálculo del Speed-up y eficiencia
        speed_up = elapsed_seq / elapsed_time
        efficiency = speed_up / size
        print(f"Speed-up: {speed_up:.2f}")
        print(f"Eficiencia: {efficiency:.2f}")

if __name__ == "__main__":
    producto_escalar()
