"""
Haz un programa que solicite número al usuario hasta que el usuario ingrese 0,
en ese caso el programa tiene que calcular la suma de los números ingresados anteriormente y el promedio

"""
num_count: int = 0
user_num: int
user_nums: list = []
num_sum: int = 0

user_num = int(input('Ingrese un numero, que sea distinto de cero = '))

while user_num != 0:
    user_nums.append(user_num)
    user_num = int(input('Ingrese un numero, que sea distinto de cero, para salir ingrese 0 = '))

#Bucle para calcular la suma

for num in user_nums:
    num_sum += num
    num_count += 1

#Calculo de promedio

print(f'La suma de los numero es {num_sum} y el promedio es de {int(num_sum / num_count)}')