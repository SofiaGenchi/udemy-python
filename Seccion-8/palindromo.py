# PRACTICA 01: PALINDROMO
"""
Crear un sistema que detecte si una palabra es palindroma o no.

Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el sistema verifica si es o no.

Una palabra "palindroma" se lee de igual forma como de la derecha y de la izquierda.
"""

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

# Funcion principal
def main():
    palabra = input('Ingrese una palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es Palindromo')
    else:
        print('No es Palindromo')

# Punto de entrada de la aplicacion
if __name__ == '__main__':
    main()