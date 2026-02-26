nombres = ["Ana", "Luis", "Marta"]

for n in nombres:
  print(n)

if "Ana" in nombres:
  print("Ana está en la lista")

# Range

for index in range(10):
  print(index)

# Acceder al indice y valor de cada elemento en una lista
for index, value in enumerate(nombres):
  print(f"El indice es {index} y el valor es {value}")


# While 

contador = 0

while contador <= 3:
  print("Contador:", contador)
  contador += 1


for n in [1, 2, 3, 4, 5]:
  if n == 3:
    continue   # salta el 3
  if n == 4:
    break      # termina el loop
  print(n)
