"""
Crear un sistema que detecte si un caracter es vocal o no.

Enunciado: dado un caracter determinar si es una vocal.

Analisis: para la solucion de este problema, se requiere que el usuario ingrese un caracter y el sistema verifique si es una vocal.
"""

vocal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

letra = input('Ingrese una letra: ')

if letra in vocal :
    print(f"{letra} es una vocal")
else :
    print(f"{letra} no es una vocal")
