from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Tiempo de inicio
start_time = MPI.Wtime()

if rank == 0:
    mensaje = "test paralelo"  # Mensaje inicial
    print(f"Soy el proceso {rank} y envío el mensaje {mensaje} al proceso {rank + 1}")
    comm.send(mensaje, dest=rank + 1)
else:
    mensaje = comm.recv(source=rank - 1)
    print(f"Soy el proceso {rank} y he recibido {mensaje}")
    if rank < size - 1:
        print(f"Soy el proceso {rank} y envío el mensaje {mensaje} al proceso {rank + 1}")
        comm.send(mensaje, dest=rank + 1)

# Tiempo final y cálculo de métricas
end_time = MPI.Wtime()
elapsed_time = end_time - start_time

total_time = comm.reduce(elapsed_time, op=MPI.MAX, root=0)
if rank == 0:
    secuential_time = total_time * size  # Tiempo secuencial supuesto
    print(f"Tiempo paralelo: {total_time:.6f} segundos")
    print(f"Tiempo secuencial supuesto: {secuential_time:.6f} segundos")
    speedup = secuential_time / total_time
    efficiency = speedup / size
    print(f"Speedup: {speedup:.6f}")
    print(f"Eficiencia: {efficiency:.6f}")

MPI.Finalize()
