#Definir una funcion 

def sayHello():
    print('Hola Mundo')

sayHello()

#Funciones con parametros 

def helloUser(name): #name es un parametro
    print(f'Hola {name}')

helloUser('Maquetose') #Maquetose es el argumento


#Argumentos posicionales 
#Se tiene en cuenta el orden en el que son asignados los parametros, a la hora de pasarle los valores
#A la función

def user_description(name,lastName):
    print(f'su nombre es {name} y su apellido es {lastName}')

user_description('Pablo','Caballero')
user_description('Caballero','Pablo')


#Argumentos nombrados 
#Especifico a que Parametro va dirigido al Argumento

name: str = 'Pablo'
last_name:str = 'Caballero'

def pre_values(name = name, last_name = last_name):
    print(f'Saludo con especificaciones para {name} {last_name}')

pre_values()


#Argumento con valor por defecto 

def predefined_value(name='Anonimus'):
    print(f'Hola mi nombre es {name}')

predefined_value()
predefined_value('Meowscarada')    

#Retornar valores con una funcion

def return_value(name='Pedro'):
    return name

pedro_pedro_pe = return_value()
print(pedro_pedro_pe)

#Type hinting en funciones

def sum (num1 : int, num2 : int) -> int:
    return num1 + num2

print(f'{sum(12,22)}')




