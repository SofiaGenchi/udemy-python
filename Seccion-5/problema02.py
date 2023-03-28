"""
Tarea: Problema 02.

Dado un rango de numeros enteros, obtener la cantidad de numeros enteros que contiene.

Analisis: Para la solucion de este problema, se requiere que el usuario ingrese un numero inicial y final, luego el sistema procesa y devuelve la cantidad de numeros enteros que contiene el rango.

Entrada:
numero inicial (n)
numero final (nf)

Salida: cantidad (c)
"""

n = int(input("Ingrese el numero inicial: "))
nf = int(input("Ingrese el numero final: "))

i = 0
c = 0

i = n + 1
while i < nf:
    c += 1
    i += 1

print(f"Cantidad: {c}")