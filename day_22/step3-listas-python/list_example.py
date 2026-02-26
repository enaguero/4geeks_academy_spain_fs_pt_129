frutas = ["manzana", "pera", "plátano"]

l = len(frutas)  # Obtiene la longitud de la lista
print("Cuantos elementos hay en la lista: ", l)
print(frutas[0])  # Imprime "manzana"

print(frutas[-1]) # Imprime "plátano", el último elemento de la lista


# Slicing (rebanado) de listas
numeros = [1, 2, 3, 4, 5, 6]

print(numeros[1:4])   # [2, 3, 4]
print(numeros[:3])    # [1, 2, 3]
print(numeros[3:])    # [4, 5, 6]


# Modificar elementos de la lista

tareas = ["estudiar", "entrenar"]

tareas.append("leer")
print(tareas)  # ['estudiar', 'entrenar', 'leer']

tareas.remove("entrenar")
print(tareas)  # ['estudiar', 'leer']

ultima = tareas.pop()
print(ultima)  # leer
print(tareas)  # ['estudiar']


# Sortear listas

nums = [8, 3, 10, 1]
nums.sort()
print(nums)  # [1, 3, 8, 10]

names= ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']