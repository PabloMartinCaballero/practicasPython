# Condicional para regresar un dato en una función

def Hello (name:str) -> str :
    return f'Hola {name or "stranger"}!'

"""
print(Hello())  Hello() missing 1 required positional argument: 'name'
                Hello esta esperando un argumento posicional
print(Hello('Meowsacarada'))

"""
