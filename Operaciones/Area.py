"""
Escribe un programa que solicite al usuario la base y la altura de un triángulo,
y calcule su área y perímetro y los muestre en pantalla con un máximo de 2 decimales

"""

base = float(input('Ingrese la base del triangulo = '))
altura = float(input('Ingrese la altura del triangulo = '))
decimales = 2

area = (base * altura)/2

## Usando round() para redondear a 2 decimales
#numero_redondeado = round(numero_float, decimales)

print(f'el valor del area es de {round(area,decimales)}')
