"""
Escribe un programa que imprima los números del 1 al 100. Pero para los múltiplos de 3,
imprime la palabra "Fizz" en lugar del número, y para los múltiplos de 5, imprime "Buzz".
Para los números que son múltiplos de tanto 3 como 5, imprime "FizzBuzz".

"""

for nums in range(1,101):
    if nums % 3 == 0 and nums % 5 == 0:
        print('FizzBuzz')
    elif nums % 5 == 0:
        print('Buzz')
    elif nums % 3 == 0:
        print('Fizz')
    else:
        print(nums)
