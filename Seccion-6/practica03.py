#  Practica 03 Guardar resultados de pares e impares
"""
Crear 2 listas y una tupla que tendra numeros de 1 a 9. La primera lista se llamara pares y el segundo impar, ambos vacios.
Despues multiplica cada uno de los numeros de la tupla por un numero aleatorio entre 1 y 100, si el resultado es par guarda ese numero en la lista de pares y si es impar en la lista de impares.
Muestra por consola -la multiplicacion que se produce junto con su resultado con el formato 2 x 3 = 6 y la lista de pares e impares
"""

import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)


for n in numeros:
    numero_random = random.randint(1, 100)
    resultado = n * numero_random

    if resultado % 2 == 0:
        print(f'{n} x {numero_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        impares.append(resultado)

print('LISTA DE PARES: ', pares)
print('LISTA DE IMPARES: ', impares)