# Instrucciones de tareas

"""Enunciado:
Crear un programa para encontrar el Area de un Circulo, usando la siguiente formula:

A = pi*r2"""

"""
Area(A) = es el area del circulo
PI: representa el valor constante pi (3.14159)
radio(r) = es el radio del circulo

Analisis: para la solucion de este problema, se requiere que el usuario ingrese el radio del circulo y el sistema procesa y obtiene el Area del circulo.

Entrada: radio
Salida: Area(a)

Se requiere que el usuario ingrese el radio del circulo y el sistema procesa y obtiene el Area del circulo.
"""

pi = 3.14159

r = float(input("Ingrese el radio del circulo: "))
r = float(r)

a = pi * r ** 2

print("El area es: ", a)