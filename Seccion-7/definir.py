def saludar():
    global nombre #hace que la variable pueda ser utilizada fuera de la funcion
    nombre = input('Ingresa tu nombre: ')
    print(f'Hola {nombre}!')

saludar()
print(f'Hola {nombre} este es un mensaje desde fuera de la funcion')