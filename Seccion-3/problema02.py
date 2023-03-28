# Tarea: Problema 02
"""Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos"""

"""
Analisis: para la solucion de este problema, se requiere que el usuario ingrese un tiempo expresado en segundos y el sistema procesa y obtiene las horas, minutos y segundos restantes.

Entrada: tiempo en segundos

Salida: horas, minutos, segundos
"""

tiempo = int(input("Ingrese la cantidad de segundos: "))

horas = tiempo // 3600
segundos = tiempo
minutos = (horas % segundos) * 60

print(f"{tiempo} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")