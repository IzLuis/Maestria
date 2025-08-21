from xmlrpc.client import ServerProxy

# Conexión al servidor
servidor = ServerProxy('http://192.168.1.67:8000/')

# Pruebas de las funciones remotas
print("2 + 3 =", servidor.suma(2, 3))
print("10 - 4 =", servidor.resta(10, 4))
print("6 * 7 =", servidor.multiplica(6, 7))
print("20 / 5 =", servidor.divide(20, 5))
print("3 ^ 4 =", servidor.potencia(3, 4))
print("5! =", servidor.factorial(5))
