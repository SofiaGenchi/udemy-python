#   Tarea: Problema 01
"""
Dado 3 numeros, devolver los numeros en orden ascendente

Analisis: para la solucion de este problema, se requiere que el usuario ingrese tres numeros, luego el sistema verifica y devuelve los numeros ordenados en forma ascendente.

Primero se debe encontrar el numero mayor, luego el numero menor y al final el numero intermedio, que es el resultado de la suma de los tres numeros

Entrada: numeros (n1, n2, n3)

Salida: numeros ordenados
"""

numeros = []

for i in range(3):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)

numeros.sort()

print("Los numeros ordenados en forma ascendente son:")
for num in numeros:
    print(num)

# Variables | Ingresar Datos.
# numero1 = int(input('Número 1: '))
# numero2 = int(input('Número 2: '))
# numero3 = int(input('Número 3: '))
 
# # Solución
 
# # Hallar el número mayor
# if numero1 > numero2 and numero1 > numero3:
#     mayor = numero1
# else:
#     if numero2 > numero1 and numero2 > numero3:
#         mayor = numero2
#     else:
#         mayor = numero3
 
# # Hallar el número menor 
# if numero1 < numero2 and numero1 < numero3:
#     menor = numero1
# else:
#     if numero2 < numero1 and numero2 < numero3:
#         menor = numero2
#     else:
#         menor = numero3

# """
# n1: 2       n1: 2       n1: 1       n1: 3       n1: 3       n1: 1
# n2: 3       n2: 1       n2: 2       n2: 2       n2: 1       n2: 3
# n3: 1       n3: 3       n3: 3       n3: 1       n3: 2       n3: 2
# """
 
# # Hallar el número intermedio 
# intermedio = 0
# if (numero1 < numero2 and numero1 > numero3) or (numero1 < numero3 and numero1 > numero2):
#     intermedio = numero1
# elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
#     intermedio = numero2
# elif (numero3 > numero2 and numero3 < numero1) or (numero3 < numero2 and numero3 > numero1):
#     intermedio = numero3

 
# # Mostrar Datos
# print(f'Mayor: {mayor}')
# print(f'Intermedio: {intermedio}')
# print(f'Menor: {menor}')