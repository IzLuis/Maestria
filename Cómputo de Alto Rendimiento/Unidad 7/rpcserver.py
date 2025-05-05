from xmlrpc.server import SimpleXMLRPCServer
import math

# Funciones disponibles remotamente
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División entre cero"
    return x / y

def potencia(x, y):
    return x ** y

def factorial(n):
    if n < 0:
        return "Error: Factorial no definido para negativos"
    return math.factorial(n)

# Crear el servidor en localhost y puerto 8000
servidor = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Servidor RPC escuchando en el puerto 8000...")

# Registrar funciones
servidor.register_function(suma, 'suma')
servidor.register_function(resta, 'resta')
servidor.register_function(multiplica, 'multiplica')
servidor.register_function(divide, 'divide')
servidor.register_function(potencia, 'potencia')
servidor.register_function(factorial, 'factorial')

# Iniciar el servidor indefinidamente
servidor.serve_forever()
