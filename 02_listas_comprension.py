# =============================================================
# EJERCICIO 2: Listas y Comprensiones
# Temas: list comprehensions, filter, map, comprehensions
#        anidadas, sets y dicts por comprensión
# Nivel: básico-intermedio → intermedio
# =============================================================

# --- 1. FILTRADO CON COMPREHENSION ---
# Dado una lista de números, devolvé solo los que son:
# a) pares
# b) múltiplos de 3
# c) pares Y mayores a 10

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 21, 24]

# pares = [...]
# multiples_de_3 = [...]
# pares_mayores_10 = [...]


# --- 2. TRANSFORMACIÓN CON COMPREHENSION ---
# Dada una lista de palabras:
# a) devolvé todas en mayúsculas
# b) devolvé solo las que tienen más de 4 letras
# c) devolvé la longitud de cada palabra

palabras = ["gato", "elefante", "sol", "python", "oso", "dinosaurio", "pez"]

# en_mayusculas = [...]
# palabras_largas = [...]
# longitudes = [...]


# --- 3. COMPREHENSION ANIDADA ---
# Generá todas las combinaciones posibles de dos listas (producto cartesiano)
# Ej: [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

lista_nums = [1, 2, 3]
lista_letras = ["a", "b", "c"]

# combinaciones = [...]


# --- 4. DICT COMPREHENSION ---
# Dado una lista de palabras, creá un diccionario donde:
# - la clave es la palabra
# - el valor es la cantidad de letras

# Ej: {"gato": 4, "elefante": 8, ...}

# diccionario_longitudes = {...}


# --- 5. APLANAR UNA LISTA DE LISTAS ---
# Convertí una lista de listas en una sola lista plana usando comprehension
# Ej: [[1,2], [3,4], [5,6]] → [1, 2, 3, 4, 5, 6]

lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# lista_plana = [...]


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# print(pares)                  # [2, 4, 6, 8, 10, 12, 18, 24]
# print(multiples_de_3)         # [3, 6, 9, 12, 15, 18, 21, 24]
# print(pares_mayores_10)       # [12, 18, 24]
# print(en_mayusculas)          # ['GATO', 'ELEFANTE', ...]
# print(palabras_largas)        # ['elefante', 'python', 'dinosaurio']
# print(longitudes)             # [4, 8, 3, 6, 3, 10, 3]
# print(combinaciones)          # [(1,'a'), (1,'b'), ..., (3,'c')]
# print(diccionario_longitudes) # {'gato': 4, 'elefante': 8, ...}
# print(lista_plana)            # [1, 2, 3, 4, 5, 6, 7, 8, 9]
