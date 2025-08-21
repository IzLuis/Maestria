from mpi4py import MPI
import numpy as np
import time

def multiplicacion_matriz_vector():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    N = size  # La matriz debe ser NxN, con N igual al número de procesos
    
    if rank == 0:
        A = np.random.rand(N, N)
        x = np.random.rand(N)
    else:
        A = None
        x = np.zeros(N)
    
    # Cada proceso recibe una fila de A
    local_A = np.zeros(N)
    comm.Scatter(A, local_A, root=0)
    
    # Se transmite el vector x a todos los procesos
    comm.Bcast(x, root=0)
    
    # Medición del tiempo en paralelo
    comm.Barrier()
    start_time = MPI.Wtime()
    
    # Cada proceso calcula su producto fila-vector
    local_result = np.dot(local_A, x)
    
    # Reunir resultados en el proceso 0
    result = None
    if rank == 0:
        result = np.zeros(N)
    comm.Gather(local_result, result, root=0)
    
    comm.Barrier()
    end_time = MPI.Wtime()
    elapsed_time = end_time - start_time
    
    if rank == 0:
        # Versión secuencial
        start_seq = time.time()
        result_seq = np.dot(A, x)
        end_seq = time.time()
        elapsed_seq = end_seq - start_seq
        
        print(f"Prueba con un tamaño de {N}x{N}")
        print(f"Resultado paralelo: {result}")
        print(f"Resultado secuencial: {result_seq}")
        print(f"Tiempo transcurrido (paralelo): {elapsed_time:.6f} segundos")
        print(f"Tiempo transcurrido (secuencial): {elapsed_seq:.6f} segundos")
        
        # Cálculo del Speed-up y eficiencia
        speed_up = elapsed_seq / elapsed_time
        efficiency = speed_up / size
        print(f"Speed-up: {speed_up:.2f}")
        print(f"Eficiencia: {efficiency:.2f}")

if __name__ == "__main__":
    multiplicacion_matriz_vector()
