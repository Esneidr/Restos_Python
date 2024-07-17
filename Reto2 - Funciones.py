# Funciones 

# Simples 

def greet():
    print("Hola, Esneider")


greet()

# Con Retorno

def return_greet():
    return "Hola, Esneider"

print(return_greet())

# Con Argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Thiago")

# Con Argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hello", "Thiago")
args_greet(name="Thiago", greet="Hello")

# Con un argumento predeterminado

def default_arg_greet(name='Thiago'):
    print(f"Hola, {name}")

default_arg_greet("Esneider")
default_arg_greet()

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hola", "Esneider"))

# Retorno con varios varoles 

def multiple_return_greet():
    return f"Hola", "Esneider"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Número de varibles de argumetos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {names}")

variable_arg_greet("Esneider", "Thiago", "Camilo")

# Con número de varibles de argumetos con palabra clave 

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})")

variable_arg_greet(name="Esneider", age=28, hijo="Thiago", hermano="Camilo")

# Funciones entre funciones

def outer_fuction():
    def innner_fuction():
        print("Funcion interna: Hola, Esneider")
        innner_fuction()

outer_fuction()

# Funcione del lenguaje

print(len("Esneider"))
print(type("Esneider"))
print("Esneider".upper())


# Ejercicio 

'''
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def print_number(text_1, text_2) -> int:
    count = 0
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print_number("multiplo_3", "multiplo_5")