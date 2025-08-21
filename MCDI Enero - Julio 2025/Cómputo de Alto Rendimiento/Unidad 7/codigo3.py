from threading import Thread, Lock
import time

# Textos que escribirá cada hilo
quijote_texto = """...En un lugar de la Mancha de cuyo nombre no
quiero acordarme, no ha mucho tiempo que vivía
un hidalgo de los de lanza en astillero, adarga
antigua, rocín flaco y galgo corredor.
Una olla de algo más vaca que carnero, salpicón
las más noches, duelos y quebrantos los sábados,
lentejas los viernes...
"""

romeo_texto = """- Habla. ¡Oh! ¡Habla otra vez ángel resplan-
deciente!. . . Porque esta noche apareces tan
esplendorosa sobre mi cabeza como un ala-
do mensajero celeste ante los ojos estáticos y
maravillados de los mortales, que se inclinan
hacia atrás para verle, cuando él cabalga so-
bre las tardas perezosas nubes y navega en
el seno del aire.
"""

julieta_texto = """¡Oh Romeo, Romeo! ¿Por qué eres tú
Romeo? Niega a tu padre y rehusa tu nom-
bre; o, si no quieres, júrame tan sólo que 
me amas, y dejaré yo de ser una Capuleto.
"""

# Variables compartidas
lock = Lock()
turno = 0  # 0 = Quijote, 1 = Romeo, 2 = Julieta

# Ruta del archivo a escribir
archivo_salida = "literatura.txt"

class Escritor(Thread):
    def __init__(self, nombre, texto, mi_turno):
        super().__init__()
        self.nombre = nombre
        self.texto = texto
        self.mi_turno = mi_turno

    def run(self):
        global turno
        while True:
            if turno == self.mi_turno:
                with lock:
                    with open(archivo_salida, "a", encoding="utf-8") as f:
                        f.write(f"\n[{self.nombre}]\n")
                        f.write(self.texto)
                    turno += 1  # pasa al siguiente escritor
                break
            else:
                time.sleep(0.1)  # Espera un poco antes de volver a revisar

# Crear hilos
quijote = Escritor("Quijote", quijote_texto, 0)
romeo = Escritor("Romeo", romeo_texto, 1)
julieta = Escritor("Julieta", julieta_texto, 2)

# Lanzar hilos
quijote.start()
romeo.start()
julieta.start()

# Esperar a que terminen
quijote.join()
romeo.join()
julieta.join()

print("Archivo escrito correctamente")