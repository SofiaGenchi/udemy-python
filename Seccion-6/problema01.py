#  Tarea: Problema 01
"""
Ingrese 6 numeros en una lista y obtenga el mayor y menor ingresado
Analisis: para la solucion de este problema, se requiere que el usuarioingrese 6 numeros, luego el sistema devuelva el numero mayor y menor.
"""



numeros = list(map(int, input("Ingrese 6 números separados por coma: ").split(",")))

minimo = maximo = numeros[0]

for numero in numeros:
    if numero < minimo:
        minimo = numero
    elif numero > maximo:
        maximo = numero

print(f'El numero mayor ingresado es {maximo} y el numero menor ingresado es {minimo}')