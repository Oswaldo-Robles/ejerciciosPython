# =============================================================
# EJERCICIO 6: Manejo de Archivos
# Temas: leer/escribir archivos, CSV manual, contexto with,
#        append, buscar en archivos
# Nivel: intermedio
# =============================================================

# --- 1. ESCRIBIR Y LEER UN ARCHIVO ---
# a) Escribí una función que reciba un nombre de archivo y una lista
#    de strings, y escriba cada string en una línea del archivo.
# b) Escribí una función que lea ese archivo y devuelva una lista
#    de strings (sin el \n al final de cada línea).

def escribir_lineas(nombre_archivo, lineas):
    pass


def leer_lineas(nombre_archivo):
    pass


# --- 2. APPEND ---
# Escribí una función que agregue una línea al final de un archivo
# sin borrar lo que ya tiene.

def agregar_linea(nombre_archivo, linea):
    pass


# --- 3. CSV MANUAL ---
# Sin usar el módulo csv, trabajá con archivos de texto separados por comas.
#
# a) Escribí una función que reciba una lista de dicts y los guarde como CSV.
#    La primera línea debe ser el encabezado (las claves del dict).
#    Ej: [{"nombre": "Ana", "edad": "30"}, {"nombre": "Luis", "edad": "25"}]
#    → archivo con:
#       nombre,edad
#       Ana,30
#       Luis,25
#
# b) Escribí una función que lea ese CSV y devuelva una lista de dicts.

def escribir_csv(nombre_archivo, lista_dicts):
    pass


def leer_csv(nombre_archivo):
    pass


# --- 4. BUSCAR EN ARCHIVO ---
# Escribí una función que reciba un archivo y una palabra,
# y devuelva una lista con los números de línea donde aparece esa palabra
# (las líneas empiezan en 1).

def buscar_en_archivo(nombre_archivo, palabra):
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# escribir_lineas("prueba.txt", ["primera línea", "segunda línea", "tercera línea"])
# print(leer_lineas("prueba.txt"))
# # ["primera línea", "segunda línea", "tercera línea"]

# agregar_linea("prueba.txt", "cuarta línea")
# print(leer_lineas("prueba.txt"))
# # ["primera línea", "segunda línea", "tercera línea", "cuarta línea"]

# personas = [
#     {"nombre": "Ana", "edad": "30", "ciudad": "Madrid"},
#     {"nombre": "Luis", "edad": "25", "ciudad": "Lima"},
#     {"nombre": "Mía", "edad": "28", "ciudad": "Madrid"},
# ]
# escribir_csv("personas.csv", personas)
# print(leer_csv("personas.csv"))
# # [{"nombre": "Ana", ...}, {"nombre": "Luis", ...}, ...]

# print(buscar_en_archivo("personas.csv", "Madrid"))
# # [2, 4]  (líneas donde aparece "Madrid")
