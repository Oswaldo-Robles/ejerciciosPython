# =============================================================
# EJERCICIO 4: Funciones Avanzadas
# Temas: *args, **kwargs, funciones como argumentos,
#        funciones lambda, closures
# Nivel: intermedio
# =============================================================

# --- 1. *args ---
# Creá una función que reciba cualquier cantidad de números
# y devuelva su suma, promedio, mínimo y máximo como dict.

def estadisticas(*args):
    pass


# --- 2. **kwargs ---
# Creá una función que construya un perfil de usuario.
# Debe aceptar cualquier campo: nombre, edad, ciudad, etc.
# Ej: crear_perfil(nombre="Ana", edad=30, ciudad="Madrid")
#   → {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

def crear_perfil(**kwargs):
    pass


# --- 3. FUNCIÓN COMO ARGUMENTO ---
# Creá una función "aplicar" que reciba una lista y una función,
# y devuelva una nueva lista con esa función aplicada a cada elemento.
# No uses map() — hacélo con un loop o comprehension.
# Ej: aplicar([1,2,3], lambda x: x**2) → [1, 4, 9]

def aplicar(lista, funcion):
    pass


# --- 4. LAMBDA ---
# Usá lambda para resolver estos casos sin definir funciones con def:

numeros = [5, 2, 8, 1, 9, 3, 7]

# a) Ordenar de mayor a menor usando sorted() con key=lambda
# ordenados = ...

# b) Filtrar solo los impares usando filter() con lambda
# impares = ...

# c) Elevar al cuadrado usando map() con lambda
# cuadrados = ...


# --- 5. CLOSURE ---
# Un closure es una función que "recuerda" el entorno donde fue creada.
# Creá una función "crear_multiplicador(n)" que devuelva una función
# que multiplica su argumento por n.
# Ej:
#   doble = crear_multiplicador(2)
#   triple = crear_multiplicador(3)
#   doble(5)  → 10
#   triple(5) → 15

def crear_multiplicador(n):
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# print(estadisticas(4, 7, 2, 9, 1))
# # {"suma": 23, "promedio": 4.6, "minimo": 1, "maximo": 9}

# print(crear_perfil(nombre="Ana", edad=30, ciudad="Madrid"))
# # {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# print(aplicar([1, 2, 3, 4], lambda x: x ** 2))
# # [1, 4, 9, 16]

# print(sorted(numeros, key=lambda x: -x))   # [9, 8, 7, 5, 3, 2, 1]
# print(list(filter(lambda x: x % 2 != 0, numeros)))  # [5, 1, 9, 3, 7]
# print(list(map(lambda x: x ** 2, numeros)))          # [25, 4, 64, 1, 81, 9, 49]

# doble = crear_multiplicador(2)
# triple = crear_multiplicador(3)
# print(doble(5))   # 10
# print(triple(5))  # 15
