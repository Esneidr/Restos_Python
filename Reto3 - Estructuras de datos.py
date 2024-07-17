# Listas
'''
(list)
Las listas son colecciones ordenadas y mutables de elementos. 
Pueden contener elementos de diferentes tipos.
'''
mi_lista = [1,2,3,4,5,6]
print(mi_lista)

# Modificar elemento
mi_lista[0] = 25
print(mi_lista)

# Agregar elemento
mi_lista.append(6) 
print(mi_lista)

# Eliminar elemeto
mi_lista.pop(0)
print(mi_lista)

# Ordenar elementos actumaticamente
mi_lista.sort()
print(mi_lista)

# Tuplas
'''
Tuple
Las tuplas son colecciones ordenadas e inmutables de elementos.
Una vez creada una tupla, no se puede modificar.
'''
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[3]) # [3] Imprime en esta posición.

# Conjuntos 
'''
Set
Los conjuntos son colecciones desordenadas de elementos únicos. 
No permiten duplicados.
'''
mi_conjunto = {1, 2, 3, 4, 5}

# Agregar elemento
mi_conjunto.add(6)
print(mi_conjunto)

# Elimimar elemento
mi_conjunto.remove(1)
print(mi_conjunto)

# Dicionarios
'''
dict
Los diccionarios son colecciones desordenas de pares clave-valor. 
Cada clave en el diccionarios es unica. 
'''

mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(mi_diccionario)

# Modificar elementos
mi_diccionario['d'] = 25
print(mi_diccionario)

# Agregar elementos 
mi_diccionario['f'] = 6
print(mi_diccionario)

# Eliminar elementos 
del mi_diccionario['f']
print(mi_diccionario)


# Ejercicio 
'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''

def mis_contactos():

    def ingresar_telefono():
        telefono = input(f"\nIngresa el número de {nombre}: ")
        if telefono.isdigit() and len(telefono) == 10:
            contactos[nombre] = telefono
        else:
            print("El número de telefono es invalido.")

    contactos = {}

    while True:
        
        print("Hola que deseas realizar hoy: ")
        print("-----------------------------")
        print("--- 1. Buscar Contacto ------")
        print("--- 2. Agregar Contacto -----")
        print("--- 3. Modificar Contacto ---")
        print("--- 4. Elimiar Contacto -----")
        print("--- 5. Salir ----------------")
        print("-----------------------------")

        opcion = input("\nSeleciona una opcion: ")

        match opcion:
            case "1":
                nombre = input("\nIngresa el nombre a buscar: ")
                if nombre in contactos:
                    print(f"El contato de {nombre} es {contactos[nombre]}.")
                else:
                    print(f"El contacto {nombre} no existe.")
            case "2":
                nombre = input("\nIngresa el nombre del nuevo contacto: ")
                if contactos.get(nombre):
                    print(f"Ya tiene un contacto llamado así: {nombre}.")
                else:
                    ingresar_telefono()
            case "3":
                nombre = input("\nIngresa el nombre a modificar: ")
                if nombre in contactos:
                    ingresar_telefono()
                else:
                    print(f"El contacto {nombre} no existe.")
            case "4":
                nombre = input("\nIngresa el nombre a eliminar: ")
                if nombre in contactos:
                    del contactos[nombre]
                    print(f"{nombre} se ha eliminado de tus contactos.")
                else:
                    print(f"El contacto {nombre} no existe.")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta; debe elegir 1 al 5. Gracias")

mis_contactos()







        
