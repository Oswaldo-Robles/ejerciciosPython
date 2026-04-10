# =============================================================
# EJERCICIO 9: Decoradores
# Temas: decoradores propios, functools.wraps,
#        decorador con argumentos, decoradores apilados
# Nivel: intermedio → intermedio-sólido
# =============================================================

from functools import wraps
import time

# --- 1. DECORADOR TIMER ---
# Creá un decorador "timer" que mida cuánto tarda en ejecutarse
# una función e imprima el tiempo en segundos.
# Usá time.time() antes y después de llamar a la función.
# Usá @wraps(func) para preservar el nombre y docstring original.

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


# --- 2. DECORADOR LOGGER ---
# Creá un decorador "logger" que imprima:
# - Antes: "Llamando a [nombre_función] con args=[...] kwargs={...}"
# - Después: "Resultado: [valor retornado]"

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


# --- 3. DECORADOR VALIDADOR DE TIPOS ---
# Creá un decorador "solo_enteros" que verifique que todos los
# argumentos posicionales sean enteros antes de ejecutar la función.
# Si alguno no lo es, lanzá TypeError con un mensaje descriptivo.

def solo_enteros(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


# --- 4. DECORADOR CON ARGUMENTOS ---
# Un decorador que acepta argumentos necesita una capa extra.
# Creá "repetir(n)" que ejecute la función n veces.
# Ej: @repetir(3) hace que la función se llame 3 veces.

def repetir(n):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass
        return wrapper
    return decorador


# --- 5. DECORADORES APILADOS ---
# Usá @timer y @logger juntos sobre una función de prueba.
# El orden importa: el decorador más cercano a la función se aplica primero.

@timer
@logger
def calcular_suma(lista):
    """Suma todos los elementos de una lista."""
    return sum(lista)


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# @timer
# def tarea_lenta():
#     time.sleep(0.5)
#     return "listo"
# tarea_lenta()   # Tiempo de ejecución: ~0.5s

# @logger
# def multiplicar(a, b):
#     return a * b
# multiplicar(3, 4)
# # Llamando a multiplicar con args=[3, 4] kwargs={}
# # Resultado: 12

# @solo_enteros
# def sumar(a, b):
#     return a + b
# print(sumar(3, 4))      # 7
# print(sumar(3, "cuatro"))  # TypeError

# @repetir(3)
# def saludar(nombre):
#     print(f"Hola, {nombre}!")
# saludar("Ana")   # imprime 3 veces

# calcular_suma([1, 2, 3, 4, 5])   # activa timer + logger
