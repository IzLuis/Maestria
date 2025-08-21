import time
from threading import Thread

class MiHilo(Thread):
    def __init__(self, num, nom):
        Thread.__init__(self)
        self.bignum = num
        self.nombre = nom

    def run(self):
        for l in range(10):              # 10 iteraciones
            for k in range(self.bignum): # trabajo pesado
                res = 0
                for i in range(self.bignum):
                    res += 1
            print(self.nombre + ": iteracion " + str(l))

def test():
    num1 = 1000
    num2 = 500
    thr1 = MiHilo(num1, "Hilo 1")
    thr2 = MiHilo(num2, "Hilo 2")
    
    thr2.start()
    thr1.start()
    
    thr1.join()
    thr2.join()

if __name__ == "__main__":
    test()