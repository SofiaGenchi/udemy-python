"""
Aplicacion de la seccion:

Crear un sistema que detecte si numero es par positivo o par negativo y tambien si es impar positivo o negativo y si el numero ingresado es 0 que detecte si es neutro.

Enunciado: determinar si un numero entero es par positivo, impar positivo, par negativo, impar negativo o neutro.

Analisis: para la solucion de este problema, se requiere que el usuario ingrese un numero entero y el sistema verifique si es par positivo, impar positivo, par negativo, impar negativo o neutro.
"""

numero = int(input("Ingrese un numero entero: "))

if numero != 0:
    if numero > 0:
        if numero % 2 == 0:
            print(f"El numero {numero} es PAR POSITIVO")
        else:
            print(f"El numero {numero} es IMPAR POSITIVO")
    else:
        if numero % 2 == 0:
            print(f"El numero {numero} es PAR NEGATIVO")
        else:
            print(f"El numero {numero} es IMPAR NEGATIVO")
else:
    print(f"El numero {numero} es NEUTRO")
