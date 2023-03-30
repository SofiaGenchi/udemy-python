def saludar():
    global nombre
    nombre = input('Ingresa tu nombre: ')
    edad = 26
    return 'Hola desde la funcion saludar', nombre, edad

valor = saludar() # lo almacena como una tupla ()
print(valor)

