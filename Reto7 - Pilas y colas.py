'''
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
'''

# Pila (Stack): El último en entrar es el primero en salir (LIFO).

stack = []
stack.append("1")
stack.append("2")
stack.append("3") # push
print(stack)

stack_item = stack[len(stack) - 1] # pop
del stack[len(stack) - 1] 
print(stack_item)
print(stack.pop())
print(stack)

# Cola (Queue): El primero en entrar es el primero en salir (FIFO).

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item  = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

'''
 * DIFICULTAD EXTRA
 * 2) Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 
 * 3) Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''

# Ejercicio 2

# web

def web_navegación():
    
    stack1 = []
    
    while True:
        
        action = input("Escoge o interectua hacia adelante/atrás/salir: ")
        
        if action == "salir":
            print("Saliendo... ")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack1) > 0:
                stack1.pop()
        else:
            stack1.append(action)
            
            if len(stack1) > 0:
                print(f"Has navegado al web: {stack1[len(stack1) - 1]}")
            else:
                print("Estás en la página de inicio.")
      
web_navegación()

# Ejercicio 3

# printed

def shared_printed():
    
    queue  = []
    
    while True:
        
        action = input(" Añade un documento o dale a imprimir/salir: ")
        
        if action == "salir":
            break     
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print("No hay documentos cargados")
        else:
            queue.append(action)
            print(f"Cola de impresión: {queue}")
            
shared_printed()
    


