import sys
from collections import defaultdict
import time

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

if __name__ == "__main__":
    reduce_words()