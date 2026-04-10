# =============================================================
# EJERCICIO 7: Programación Orientada a Objetos
# Temas: clases, herencia, __str__, __repr__,
#        métodos especiales, polimorfismo básico
# Nivel: intermedio
# =============================================================

# --- 1. CLASE BASE ---
# Creá una clase Vehiculo con:
# - Atributos: marca, modelo, año, velocidad_actual (inicia en 0)
# - Métodos:
#   - acelerar(cantidad): suma cantidad a velocidad_actual
#   - frenar(cantidad): resta cantidad, mínimo 0
#   - __str__: devuelve "Marca Modelo (año) - velocidad: X km/h"

class Vehiculo:
    pass


# --- 2. HERENCIA ---
# Creá dos clases que hereden de Vehiculo:
#
# Auto:
# - Atributo extra: cantidad_puertas
# - __str__: agrega "- X puertas" al final del str del padre
#
# Moto:
# - Atributo extra: tiene_sidecar (bool)
# - __str__: agrega "- con sidecar" o "- sin sidecar"

class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


# --- 3. __repr__ ---
# Agregá __repr__ a Vehiculo para que muestre algo útil
# cuando el objeto aparece en una lista o en el intérprete.
# Ej: Vehiculo(marca='Toyota', modelo='Corolla', año=2020)


# --- 4. CLASE CON VALIDACIÓN ---
# Creá una clase Temperatura con:
# - Atributo: _celsius (privado por convención)
# - Property celsius: getter y setter (el setter valida que no baje de -273.15)
# - Property fahrenheit: solo getter, convierte de celsius
# - Property kelvin: solo getter, convierte de celsius
# - __str__: "X°C / Y°F / Z K"

class Temperatura:
    pass


# =============================================================
# PRUEBAS — descomenta para verificar
# =============================================================

# v = Vehiculo("Toyota", "Corolla", 2020)
# v.acelerar(60)
# v.frenar(20)
# print(v)   # Toyota Corolla (2020) - velocidad: 40 km/h

# a = Auto("Ford", "Focus", 2022, 4)
# a.acelerar(100)
# print(a)   # Ford Focus (2022) - velocidad: 100 km/h - 4 puertas

# m = Moto("Honda", "CBR", 2021, False)
# print(m)   # Honda CBR (2021) - velocidad: 0 km/h - sin sidecar

# flota = [v, a, m]
# print(flota)   # usa __repr__

# t = Temperatura(100)
# print(t)           # 100°C / 212.0°F / 373.15 K
# t.celsius = -300   # lanza ValueError
