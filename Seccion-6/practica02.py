#  Practica 02: Descuento de un restaurante parte 02
"""
Enunciado: debido a los excelentes resultados, el restaurante decide ampliar sus ofertas de acuerdo a la siguiente escala de consumo.
Determinar el monto del decuento, el importe del impuesto y el importe a pagar.

Consumo hasta 100 --- descuento de 10%
Consumo mayor a 100 --- descuento de 20%
Consumo mayo a 200 --- descuento de 30%


Analisis: para la solucion de este problema, se requiere que el usiario ingrese el consumo y el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.
"""

consumo = float(input('Ingrese el consumo del cliente: '))
if consumo >= 0:
    if consumo <= 100:
        # Descuento del 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        # Descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        # Descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30

    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19
    total_pagar = monto_descuento + igv

    #  Salida de datos
    print('=' * 30)
    print('--- FACTURA DE CONSUMO ---')
    print('Descuento que se aplica: ', dato_descuento)
    print('=' * 30)
    print('Consumo: ', consumo)
    print('Descuento: ', descuento)
    print('Monto con descuento: ', monto_descuento)
    print('IGV: ', igv)
    print('Total a Pagar: ', total_pagar)
    print('=' * 30)
else:
    print('Error al ingresar el consumo')