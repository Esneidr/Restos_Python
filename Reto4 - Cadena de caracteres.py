'''
En Python, una cadena de caracteres (o simplemente una cadena) es una secuencia 
de caracteres encerrada entre comillas simples (') o dobles ("). 
Las cadenas son inmutables, lo que significa que una vez creadas, no se pueden modificar. 
Sin embargo, se pueden realizar diversas operaciones con ellas, 
como concatenación, repetición, y acceso a caracteres individuales o subcadena.
'''

cadena1 = 'Hola, Mundo!'
cadena2  ="Este lenguaje es Python"

# Concatenacion 
cadena3 = cadena1 + ' ' + cadena2
print(cadena3)

# Repeticiion
cadena4 = 'Programación ' * 3
print(cadena4)

# Acesso a caracteres individuales
caracter = cadena1[1]
print(caracter)

# Subacadenas (slicing)
subcadena = cadena2[5:14]
print(subcadena)

# Longitud
longuitud = len(cadena3)
print(longuitud)

# Comillas triples para cadenas multilínea
cadena_multilinea = """Esta es una cadena
que abarca
múltiples líneas."""
print(cadena_multilinea)

# Recorrido 
for cadena5 in 'Lenguaje Python':
    print(cadena5)

# Conversion 
cadena6 = 'Hola, Esneider'
cadena_mayuscula = cadena6.upper()
cadena_minuscula = cadena6.lower()

print(cadena_mayuscula)
print(cadena_minuscula)

# Reemplazo
cadena7 = "Hola, Esneider"
cadena_nueva = cadena7.replace("Esneider", "Antonio")

print(cadena7)
print(cadena_nueva)

# Division 
cadena8 = 'Hola, mundo, Python'
partes = cadena8.split(', ')

print(partes)

# Union
partes  =['Hola', 'mundo', 'Python']
cadena_unidad = ', '.join(partes)

print(cadena_unidad)

# Interpolación
nombre = 'Esneider'
edad = 28
interpolacion = f'El aspirante {nombre} de {edad} años, fue admito para el cargo: Analista de datos'

print(interpolacion)

# Verificación
'''
Puedes usar varios métodos para verificar el contenido de una cadena:

startswith(): Verifica si la cadena comienza con una subcadena específica.
endswith(): Verifica si la cadena termina con una subcadena específica.
isnumeric(): Verifica si todos los caracteres de la cadena son números.
isalnum(): Verifica si la cadena contiene solo caracteres alfanuméricos.
isspace(): Verifica si la cadena contiene solo espacios en blanco.
in: Verifica si una subcadena está presente en la cadena.
'''
cadena = "Python es un lenguaje facil de aprender"
print(cadena.startswith("Python"))  # True
print(cadena.endswith("lenguaje"))  # True
print(cadena.isnumeric())  # False
print("es" in cadena)  # True

# Ejercicio 

'''
Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

def chek(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        
        return isogram
    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")

chek("radar", "pythonpythonpythonpython")
#chek("amor", "roma")