# =============================================================
# EJERCICIO 10: Generadores
# Temas: yield, generadores infinitos, next(), itertools básico,
#        generator expressions, send()
# Nivel: intermedio → intermedio-sólido
# =============================================================

# --- 1. GENERADOR BÁSICO CON YIELD ---
# Creá un generador que produzca los números del 1 al n de uno en uno.
# A diferencia de una lista, no genera todos los valores en memoria.

def contar_hasta(n):
    pass


# --- 2. GENERADOR INFINITO ---
# Creá un generador que produzca números de Fibonacci infinitamente.
# No tiene fin — quien lo use decide cuándo parar.
# Usalo con next() o con un loop con break.

def fibonacci_infinito():
    pass


# --- 3. GENERADOR DE PIPELINE ---
# Los generadores se pueden encadenar como tuberías (pipeline).
# Creá tres generadores:
# a) leer_numeros(lista): produce cada número de la lista
# b) solo_pares(generador): filtra solo los pares
# c) al_cuadrado(generador): eleva cada número al cuadrado
#
# Luego encadenalos para procesar la lista sin crear listas intermedias.

def leer_numeros(lista):
    pass

def solo_pares(generador):
    pass

def al_cuadrado(generador):
    pass


# --- 4. GENERATOR EXPRESSION ---
# Similar a list comprehension pero con () en lugar de [].
# No crea la lista completa en memoria.
# Creá una generator expression que genere los cuadrados del 1 al 100
# y usá next() para obtener los primeros 5 valores.

# gen = (...)


# --- 5. GENERADOR CON SEND() ---
# send() permite enviarle un valor al generador desde afuera.
# Creá un generador "acumulador" que:
# - Reciba números con send()
# - Lleve la suma acumulada
# - Yield la suma actual en cada paso

def acumulador():
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# gen = contar_hasta(5)
# print(next(gen))   # 1
# print(next(gen))   # 2
# print(list(contar_hasta(5)))  # [1, 2, 3, 4, 5]

# fib = fibonacci_infinito()
# primeros_10 = [next(fib) for _ in range(10)]
# print(primeros_10)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pipeline = al_cuadrado(solo_pares(leer_numeros(numeros)))
# print(list(pipeline))   # [4, 16, 36, 64, 100]

# gen = (x**2 for x in range(1, 101))
# print([next(gen) for _ in range(5)])   # [1, 4, 9, 16, 25]

# acc = acumulador()
# next(acc)          # inicializar
# print(acc.send(10))   # 10
# print(acc.send(20))   # 30
# print(acc.send(5))    # 35
