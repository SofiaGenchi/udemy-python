# Actividad 03: GENERADOR DE CONTRASEÑAS

"""
Crear un sistema que genere una contraseña aleatoria.

Para la solucion de este problema se requiere de listas, listas mayusculas, listas minusculas, lista de numeros y lista de simbolos, luego armar una constraseña aleatoria sacando caracteres de estas listas.
"""

import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['$', '!', '+', '.']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contra = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contra.append(caracter_random)

    contra = "".join(contra)
    return contra

def main():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ', contrasena)

if __name__ == '__main__':
    main()