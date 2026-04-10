# =============================================================
# EJERCICIO 1: Strings Avanzado
# Temas: slicing, métodos de string, palíndromos, anagramas, cifrado César y más
# Nivel: básico-intermedio → intermedio
# =============================================================

# --- 1. PALÍNDROMO ---
# Un palíndromo es una palabra que se lee igual al derecho y al revés.
# Ej: "reconocer", "anilina", "kayak"

def es_palindromo(texto):
    # Tip: ignorá mayúsculas y espacios antes de comparar
    texto = texto.lower().replace(" ", "")
    pass  # reemplazá esto con tu lógica


# --- 2. ANAGRAMA ---
# Dos palabras son anagramas si tienen exactamente las mismas letras.
# Ej: "amor" y "roma", "listen" y "silent"

def son_anagramas(palabra1, palabra2):
    # Tip: sorted() sobre un string devuelve lista de caracteres ordenados
    pass


# --- 3. CIFRADO CÉSAR ---
# Desplaza cada letra del texto N posiciones en el alfabeto.
# Ej: cifrar("abc", 3) → "def"  /  cifrar("xyz", 2) → "zab"

def cifrar_cesar(texto, desplazamiento):
    # Tip: usá ord() para obtener el número ASCII de una letra
    # y chr() para convertir un número de vuelta a letra
    # ord('a') = 97, ord('z') = 122
    pass


def descifrar_cesar(texto, desplazamiento):
    # Tip: descifrar es cifrar con desplazamiento negativo
    pass


# =============================================================
# PRUEBAS — descomenta para probar cada función
# =============================================================

# print(es_palindromo("Reconocer"))       # True
# print(es_palindromo("Hola"))            # False
# print(son_anagramas("amor", "roma"))    # True
# print(son_anagramas("perro", "gato"))   # False
# print(cifrar_cesar("hola", 3))          # "krod"
# print(descifrar_cesar("krod", 3))       # "hola"
