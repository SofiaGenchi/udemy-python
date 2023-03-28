"""
Suma de numeros anteriores

Enunciado: obtener la suma de los dos primeros numeros natural positivo

Analisis: para la solucion de este problema, se requiere que el usuario ingrese un numero y el sistema realice el proceso para devolver la suma de los N primeros numeros
"""

n = int(input("Ingrese un numero: "))

suma = 0

menores_n = 0

while menores_n < n:
    suma += menores_n
    menores_n += 1
print("La suma es:", suma)