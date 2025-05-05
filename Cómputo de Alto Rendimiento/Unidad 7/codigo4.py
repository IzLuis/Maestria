from threading import Thread
import sys

# Clase que hereda de Thread para contar palabras en un archivo
class ContadorPalabras(Thread):
    def __init__(self, archivo, resultados, indice):
        super().__init__()
        self.archivo = archivo          # Nombre del archivo a procesar
        self.resultados = resultados    # Lista compartida para guardar los resultados
        self.indice = indice            # Posición que le corresponde en esa lista

    def run(self):
        try:
            # Abre el archivo en modo lectura
            with open(self.archivo, 'r', encoding='utf-8') as f:
                texto = f.read()                   # Lee todo el contenido
                palabras = texto.split()           # Separa por espacios (simplificado)
                cantidad = len(palabras)           # Cuenta las palabras
                self.resultados[self.indice] = (self.archivo, cantidad)  # Guarda el resultado
        except FileNotFoundError:
            # Si el archivo no existe, guarda un mensaje de error en su lugar
            self.resultados[self.indice] = (self.archivo, "Archivo no encontrado")

# Punto de entrada principal
if __name__ == "__main__":
    # Validación de argumentos
    if len(sys.argv) < 2:
        print("Uso: python cuenta_palabras.py archivo1 archivo2 ...")
        sys.exit(1)

    archivos = sys.argv[1:]                   # Lista de nombres de archivos desde la línea de comandos
    resultados = [None] * len(archivos)       # Lista vacía con la misma cantidad de entradas
    hilos = []                                

    # Se crea un hilo por archivo
    for i, archivo in enumerate(archivos):
        hilo = ContadorPalabras(archivo, resultados, i)
        hilo.start()
        hilos.append(hilo)

    # Espera a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    total_palabras = 0

    # Muestra los resultados y calcula el total
    for archivo, cantidad in resultados:
        print(f"{archivo}: {cantidad} palabras")
        if isinstance(cantidad, int):  # Suma solo si no hubo error
            total_palabras += cantidad

    print(f"total: {total_palabras} palabras")
