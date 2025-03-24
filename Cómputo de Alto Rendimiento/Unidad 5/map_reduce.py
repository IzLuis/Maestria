import sys
from collections import defaultdict
import time

# Función que implementa la fase de "Map" en el modelo MapReduce
def map_words():
    """
    Fase Map: Lee líneas de texto desde la entrada estándar (sys.stdin),
    divide cada línea en palabras y emite pares palabra\t1.
    """
    # Inicia un temporizador para medir el tiempo de ejecución
    start_time = time.time()
    
    # Lee líneas de la entrada estándar
    for line in sys.stdin:
        # Divide la línea en palabras
        words = line.strip().split()
        # Emite cada palabra con un conteo inicial de 1
        for word in words:
            print(f"{word}\t1")
    
    # Calcula el tiempo total de ejecución
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprime el tiempo transcurrido en la salida de error estándar (sys.stderr)
    print(f"Tiempo transcurrido (Map): {elapsed_time:.6f} segundos", file=sys.stderr)

# Función que implementa la fase de "Reduce" en el modelo MapReduce
def reduce_words():
    """
    Fase Reduce: Lee pares palabra\tconteo desde la entrada estándar (sys.stdin),
    agrupa las palabras y suma sus conteos totales.
    """
    # Inicia un temporizador para medir el tiempo de ejecución
    start_time = time.time()
    
    # Diccionario para almacenar la cuenta de cada palabra
    # defaultdict(int) inicializa automáticamente los valores en 0
    word_counts = defaultdict(int)
    
    # Lee líneas de la entrada estándar
    # Cada línea contiene una palabra y su cuenta separadas por un tabulador
    for line in sys.stdin:
        word, count = line.strip().split("\t")  # Divide la línea en palabra y cuenta
        word_counts[word] += int(count)        # Suma la cuenta al total de la palabra
    
    # Itera sobre las palabras y sus cuentas, ordenadas alfabéticamente
    for word, count in sorted(word_counts.items()):
        # Imprime cada palabra y su cuenta separadas por un tabulador
        print(f"{word}\t{count}")
    
    # Calcula el tiempo total de ejecución
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprime el tiempo transcurrido en la salida de error estándar (sys.stderr)
    print(f"Tiempo transcurrido (Reduce): {elapsed_time:.6f} segundos", file=sys.stderr)

# Punto de entrada del script
if __name__ == "__main__":
    """
    Dependiendo del argumento proporcionado al script, ejecuta la fase Map o Reduce.
    """
    if len(sys.argv) != 2:
        print("Uso: python map_reduce.py [map|reduce]", file=sys.stderr)
        sys.exit(1)
    
    # Determina si ejecutar la fase Map o Reduce
    phase = sys.argv[1].lower()
    if phase == "map":
        map_words()
    elif phase == "reduce":
        reduce_words()
    else:
        print("Argumento no válido. Usa 'map' o 'reduce'.", file=sys.stderr)
        sys.exit(1)