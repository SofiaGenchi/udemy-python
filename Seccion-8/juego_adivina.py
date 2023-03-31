# Practica 05: Juego - Adivina el numero

"""
Crear un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar el numero.

Para crear este juego ten en cuenta los siguientes datos:
-- Dificil: 5 intentos
-- Intermedio: 7 intentos
-- Facil: 10 intentos

De acuerdo como va intentado el juego le debe dar una pista si el numero es mas grande o mas pequeño.

Tambien tiene que indicarle las vidas que le quedan.
"""

import random

def jugar(vidas):
    numero_random = random.randint(1, 100)
    numero_elegido = None

    while numero_random != numero_elegido:
        numero_elegido = int(input('Ingrese un numero entre 1 y 100: '))

        if numero_random < numero_elegido:
            print('Elige un numero mas pequeño')
            vidas -= 1
        elif numero_random > numero_elegido:
            print('Elige un numero mas grande')
            vidas -= 1
        
        if vidas == 0:
            print(f'GAME OVER - El numero era: {numero_random}')
            break

        print(f'Te quedan {vidas} vidas')

        if numero_elegido == numero_random:
            print('FELICIDADES GANASTE')

def main():
    while True:
        menu = """
        ADIVINA EL NUMERO ALEATORIO
        1- Nivel Facil
        2- Nivel Intermedio
        3- Nivel Dificil
        4- Salir
        INGRESE UNA OPCION: """
        opcion = input(menu)

        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print('CERRANDO JUEGO')
            break
        else:
            print('Opcion incorrecta vuelva a ingresar')

if __name__ == '__main__':
    main()