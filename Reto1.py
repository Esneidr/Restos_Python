#01 OPERADORES Y ESTRUCTURAS DE CONTROL

#Suma, resta, muitplicion y división entre dos valores 

num1 = 4
num2 = 2

Suma = num1 + num2
Resta = num1 - num2 
Multiplicacion = num1 * num2
Division = num1 / num2
Division_Entera = num1 // num2
Exponencia = num1 ** num2
Modulo = num1 % num2
print( num1,'+',num2,'=',Suma)
print( num1,'-',num2,'=',Resta)
print( num1,'x',num2,'=',Multiplicacion)
print( num1,'/',num2,'=',Division)
print( num1,'/',num2,'=',Division_Entera)
print( num1, '^', num2, '=', Exponencia)
print(Modulo)

print('------------------------------------------')
#EXTRA
i = 10
x = 55
for numeros in range(i,x + 1):
    if numeros % 3 and numeros != 16:
       print(numeros, end=' ')

print('------------------------------------------')

#Operadores

print(f"Suma: 25 + 5 = {25 + 5}")
print(f"Resta: 25 - 5 = {25 - 5}")
print(f"Multilpicación: 25 * 5 = {25 * 5}")
print(f"División: 25 / 5 = {25 / 5}")
print(f"Modulo: 25 % 5 = {25 % 5}")
print(f"Exponente: 25 ** 5 = {25 ** 5}")
print(f"División Entera: 25 // 5 = {25 // 5}")

print('------------------------------------------')

#Operadores de comperación

print(f"Igualdad: 25 == 5 es {25 == 5}")
print(f"Desigualdad: 25 != 5 es {25 != 5}")
print(f"Mayor que: 25 > 5 es {25 > 5}")
print(f"Menor que: 25 < 5 es {25 < 5}")
print(f"Mayor o igual que: 25 >= 25 es {25 >= 25}")
print(f"Menor o igual que: 25 <= 5 es {25 <= 5}")

#Operadores de lógicos
print(f"AND &&: 25 + 5 == 30 AND 25 > 5 es {25 + 5 == 30 and 25 > 5}")
print(f"OR ||: 25 + 5 == 30 OR 25 > 5 es {25 + 5 == 30 or 25 > 5}")  
print(f"NOT !: NOT 25 + 5 == 25 es {not 25 + 5 == 25}") 

#Operadpres de asignación
numero = 5 # Asignación
print(numero)

numero += 1 # suma y Asignación
print(numero)

numero -= 1 # resta y Asignación
print(numero)

numero *= 1 # multiplicación y Asignación
print(numero)

numero /= 1 # división y Asignación
print(numero)

# Operadores de pertenencia 
print(f" 'e' in 'esneider' = {'e' in 'esneider'}")

# Condicionales 

my_string = "Esneider"

if my_string == "Esneider":
    print("My string es 'Esneider'")
elif my_string == "Cordoba":
    print("My string es 'Cordoba'")
else:
    print("Nombre incorrecto")

# Interactivas 

for i in range(25):
    print(i)

i = 0

while i <= 25:
    print(i)
    i += 1


# Excepciones 

try:
    print(25 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de Excepciones")


# Ejercicio 

for number in range(10, 56):
    if number % 2 == 0 and number % 3 == 0 and number !=16:
        print(number)
    


