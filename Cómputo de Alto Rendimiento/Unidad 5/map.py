import sys
import time
import re

def map_words():
    """
    Fase Map: Lee líneas de texto desde la entrada estándar (sys.stdin),
    elimina caracteres especiales excepto ñ y letras con acentos,
    convierte a minúsculas, divide cada línea en palabras y emite pares palabra\t1.
    """
    # Inicia un temporizador para medir el tiempo de ejecución
    start_time = time.time()
    
    # Lee líneas de la entrada estándar
    for line in sys.stdin:
        # Elimina caracteres especiales excepto letras con acentos y ñ
        clean_line = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]', '', line).lower()
        # Divide la línea en palabras
        words = clean_line.strip().split()
        # Emite cada palabra con un conteo inicial de 1
        for word in words:
            print(f"{word}\t1")
    
    # Calcula el tiempo total de ejecución
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprime el tiempo transcurrido en la salida de error estándar (sys.stderr)
    print(f"Tiempo transcurrido (Map): {elapsed_time:.6f} segundos", file=sys.stderr)

if __name__ == "__main__":
    map_words()