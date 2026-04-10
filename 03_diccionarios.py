# =============================================================
# EJERCICIO 3: Diccionarios
# Temas: conteo de frecuencias, inversión de dicts,
#        merge con lógica, agrupación, dict anidados
# Nivel: básico-intermedio → intermedio
# =============================================================

# --- 1. CONTEO DE FRECUENCIAS ---
# Dada una lista de palabras, contá cuántas veces aparece cada una.
# No uses Counter de collections, hacélo a mano con un dict.
# Ej: ["gato", "perro", "gato"] → {"gato": 2, "perro": 1}

def contar_frecuencias(lista):
    pass


# --- 2. INVERTIR UN DICCIONARIO ---
# Dado un dict, devolvé uno nuevo donde claves y valores están intercambiados.
# Ej: {"a": 1, "b": 2} → {1: "a", 2: "b"}
# ¿Qué pasa si hay valores duplicados? Manejá ese caso.

def invertir_diccionario(diccionario):
    pass


# --- 3. MERGE CON LÓGICA ---
# Dados dos diccionarios con claves numéricas, mergeálos en uno solo.
# Si una clave aparece en ambos, sumá los valores.
# Ej: {a:1, b:2} + {b:3, c:4} → {a:1, b:5, c:4}

def merge_sumando(dict1, dict2):
    pass


# --- 4. AGRUPAR POR CATEGORÍA ---
# Dada una lista de tuplas (nombre, categoría), creá un dict donde
# cada clave es una categoría y el valor es una lista de nombres.
# Ej: [("perro","animal"), ("rosa","planta"), ("gato","animal")]
#   → {"animal": ["perro", "gato"], "planta": ["rosa"]}

def agrupar_por_categoria(lista_tuplas):
    pass


# --- 5. DICT ANIDADO — AGENDA ---
# Creá una agenda de contactos como dict anidado:
# {
#   "Ana": {"telefono": "123", "email": "ana@mail.com"},
#   "Luis": {"telefono": "456", "email": "luis@mail.com"}
# }
# Luego escribí funciones para:
# a) agregar un contacto
# b) obtener el email de un contacto (si no existe, devolvé "No encontrado")
# c) eliminar un contacto

agenda = {}

def agregar_contacto(nombre, telefono, email):
    pass

def obtener_email(nombre):
    pass

def eliminar_contacto(nombre):
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# print(contar_frecuencias(["gato", "perro", "gato", "pez", "perro", "gato"]))
# # {"gato": 3, "perro": 2, "pez": 1}

# print(invertir_diccionario({"a": 1, "b": 2, "c": 3}))
# # {1: "a", 2: "b", 3: "c"}

# print(merge_sumando({"a": 1, "b": 2}, {"b": 3, "c": 4}))
# # {"a": 1, "b": 5, "c": 4}

# datos = [("perro","animal"), ("rosa","planta"), ("gato","animal"), ("tulipan","planta")]
# print(agrupar_por_categoria(datos))
# # {"animal": ["perro", "gato"], "planta": ["rosa", "tulipan"]}

# agregar_contacto("Ana", "123-456", "ana@mail.com")
# agregar_contacto("Luis", "789-012", "luis@mail.com")
# print(obtener_email("Ana"))       # "ana@mail.com"
# print(obtener_email("Pedro"))     # "No encontrado"
# eliminar_contacto("Luis")
# print(agenda)                     # solo queda Ana
