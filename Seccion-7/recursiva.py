def factorial(n):
    # print('Valor inicial =>', n)
    if n > 1:
        n = n * factorial(n - 1)
    
    # print('Valor final =>', n)
    return n

n = int(input('Ingrese un numero: '))

f = factorial(n)
print(f'Su Factorial de {n} es: {f}')