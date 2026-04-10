# =============================================================
# EJERCICIO 8: Recursión
# Temas: casos base, pila de llamadas, fibonacci, factorial,
#        búsqueda binaria, aplanar listas anidadas
# Nivel: intermedio
# =============================================================

# --- 1. FACTORIAL ---
# n! = n * (n-1) * (n-2) * ... * 1
# Caso base: 0! = 1
# Ej: factorial(5) → 120

def factorial(n):
    pass


# --- 2. FIBONACCI ---
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
# Ej: fibonacci(7) → 13
#
# Tip: la versión recursiva pura es lenta para n grande.
# Implementá también una versión con memoización usando un dict.

def fibonacci(n):
    pass


def fibonacci_memo(n, memo={}):
    pass


# --- 3. BÚSQUEDA BINARIA RECURSIVA ---
# Dada una lista ORDENADA y un target, devolvé el índice donde está.
# Si no está, devolvé -1.
# Lógica: comparar con el elemento del medio, descartar mitad izquierda o derecha.

def busqueda_binaria(lista, target, inicio=0, fin=None):
    pass


# --- 4. APLANAR LISTA ANIDADA (profundidad arbitraria) ---
# Convertí una lista con sublistas de cualquier profundidad en una lista plana.
# Ej: [1, [2, [3, [4]], 5]] → [1, 2, 3, 4, 5]
# Tip: usá isinstance(elemento, list) para saber si es lista

def aplanar(lista):
    pass


# --- 5. POTENCIA ---
# Calculá base**exponente sin usar el operador **
# usando recursión y la propiedad: base^n = base * base^(n-1)
# Caso base: base^0 = 1

def potencia(base, exponente):
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# print(factorial(5))    # 120
# print(factorial(0))    # 1

# print(fibonacci(7))    # 13
# print(fibonacci(10))   # 55
# print(fibonacci_memo(35))  # 9227465 (rápido con memo)

# lista_ord = [1, 3, 5, 7, 9, 11, 13, 15]
# print(busqueda_binaria(lista_ord, 7))    # 3
# print(busqueda_binaria(lista_ord, 6))    # -1

# print(aplanar([1, [2, [3, [4]], 5]]))    # [1, 2, 3, 4, 5]
# print(aplanar([[1, 2], [3, [4, [5]]]]))  # [1, 2, 3, 4, 5]

# print(potencia(2, 10))   # 1024
# print(potencia(3, 4))    # 81
