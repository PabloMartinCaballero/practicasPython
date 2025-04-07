"""

Escribe un programa que solicite tres números, calcule y muestre su promedio. Da la respuesta con un decimal.

"""

num1 = float(input('Ingrese el primer numero = '))
num2 = float(input('Ingrese el segundo = '))
num3 = float(input('Ingrese el tercero = '))

promedio:float = (num1+num2+num3)/3

print(f'El promedio es de {round(promedio,1)}')
