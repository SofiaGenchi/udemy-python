# FUNCIONES LAMBDA

"""
Pequeñas funciones anonimas pueden ser creadas con la palabra reservada lambda. Esta funcion retorna la suma de sus dos argumentos:
lambda a, b: a+b
Las funciones lambda pueden ser usadas en cualquier lugar donde sea requerido un objeto de tipo funcion.
Estan sitacticamente restringidas a una sola expresion.

"""
def sumar(a,b):
    return a + b


# una forma mas simple:
sumar_simple = lambda a,b:a+b

print(sumar_simple(10, 20))


par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0
# devuelve valores bool
print(par(4))
print(impar(12))

revertir = lambda cadena: cadena[::-1]
print(revertir('hola'))