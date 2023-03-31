# Practica 04: Conversor de Monedas
"""
Crear un sistema que convierta de moneda nacional a dolares por ejemplo.

Para solucionar este problema se requiere que el usuario ingrese la cantidad de mondas nacionales y luego realizar la conversion.

Para este sistemadebe hacer un menu de navgecion para seleccionar a que tipo de moneda se hara la conversion y tambien para cerrar el programa, el sistema no se debe cerrar si no se desea.
"""

def conversor(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'Tienes $${dolares} Dolares')


def main():
    while True:
        menu = """
        1- Soles Peruanos a Dolares
        2- Pesos Mexicanos a Dolares
        3- Pesos Colombianos a Dolares
        4- Salir
        Ingrese una Opcion: 
        """
        opcion = input(menu)

        if opcion == '1':
            conversor(3.61, 'soles peruanos')
        elif opcion == '2':
            conversor(20.01, 'pesos mexicanos')
        elif opcion == '3':
            conversor(3471.27, 'Pesos Colombianos')
        elif opcion == '4':
            print('Cerrando conversor de monedas')
            break
        else:
            print('Opcion incorrecta!')
            print('Vuelve a ingresar la opcion correcta')

if __name__ == '__main__':
    main()