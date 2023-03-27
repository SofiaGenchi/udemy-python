"""Practica 01:
Calcular cociente y el Residuo de dos numeros enteros
"""
# Enunciado: hallar el cociente y el residuo (resto) de dos numeros enteros

# Analisis: para la solucion de este problema, se requiere que el usuario ingrese dos numeros enteros y el sistema realice el calculo respectivo para hallar el cociente y residuo.

print("Calcular cociente y residuo")

a = input("Ingrese el primer numero: ")
b = input("Ingrese el segundo numero: ")

a = int(a)
b = int(b)

cociente = a // b
residuo = a % b

print("El cociente es: ", cociente)
print("El residuo es: ", residuo)