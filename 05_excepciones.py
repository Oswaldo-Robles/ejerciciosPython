# =============================================================
# EJERCICIO 5: Manejo de Excepciones
# Temas: try/except, múltiples excepciones, else/finally,
#        excepciones propias, context managers (with)
# Nivel: intermedio
# =============================================================

# --- 1. TRY / EXCEPT BÁSICO ---
# Escribí una función que divida dos números.
# Si el divisor es 0, capturá el error y devolvé None.
# Si alguno no es número, capturá el error y devolvé None.

def dividir(a, b):
    pass


# --- 2. MÚLTIPLES EXCEPCIONES ---
# Escribí una función que reciba una lista y un índice,
# y devuelva el elemento en ese índice convertido a entero.
# Manejá por separado:
# - IndexError: índice fuera de rango
# - ValueError: el elemento no se puede convertir a int

def obtener_entero(lista, indice):
    pass


# --- 3. ELSE Y FINALLY ---
# else se ejecuta si NO hubo excepción.
# finally se ejecuta SIEMPRE, haya o no excepción.
#
# Escribí una función que simule abrir un archivo (sin leerlo de verdad).
# Usá un dict como "base de datos" de archivos disponibles.
# Si el archivo existe, devolvé su contenido (else).
# Si no existe, lanzá FileNotFoundError.
# En ambos casos, imprimí "Operación finalizada" (finally).

archivos_disponibles = {
    "config.txt": "host=localhost\nport=8080",
    "datos.txt": "nombre,edad\nAna,30\nLuis,25"
}

def leer_archivo_simulado(nombre):
    pass


# --- 4. EXCEPCIÓN PROPIA ---
# Creá una excepción personalizada llamada SaldoInsuficienteError.
# Luego creá una clase CuentaBancaria con:
# - saldo inicial
# - método depositar(monto)
# - método retirar(monto) → lanza SaldoInsuficienteError si no hay saldo

class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    def __init__(self, saldo_inicial):
        pass

    def depositar(self, monto):
        pass

    def retirar(self, monto):
        pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# print(dividir(10, 2))      # 5.0
# print(dividir(10, 0))      # None
# print(dividir(10, "a"))    # None

# print(obtener_entero(["3", "7", "abc", "1"], 1))   # 7
# print(obtener_entero(["3", "7", "abc", "1"], 2))   # None (ValueError)
# print(obtener_entero(["3", "7"], 10))               # None (IndexError)

# leer_archivo_simulado("config.txt")   # imprime contenido + "Operación finalizada"
# leer_archivo_simulado("nope.txt")     # error + "Operación finalizada"

# cuenta = CuentaBancaria(100)
# cuenta.depositar(50)
# print(cuenta.saldo)    # 150
# cuenta.retirar(200)    # lanza SaldoInsuficienteError
