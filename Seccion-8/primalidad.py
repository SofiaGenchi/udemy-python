# Practica 02: PRIMALIDAD

"""
Crear un sistema que detecte si un numero es primo o no.

Para la solucionar este problema se requiere que el usuario ingrese un numero por teclado y el sistema detecte si es primo o no.

Un numero primo es aquel que se puede dividir solo por 1 y por si mismo.
"""

def es_primo(numero):
    contador = 0

    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue

        # Verifica que la division con los numeros hasta el numero ingresado sea igual a 0
        if numero % i == 0:
            contador += 1
    
    if contador == 0:
        return True
    else:
        return False

def main():
    nuemero = int(input('Ingrese un numero: '))

    if es_primo(nuemero):
        print('Es Primo')
    else:
        print('No es Primo')


if __name__ == '__main__':
    main()