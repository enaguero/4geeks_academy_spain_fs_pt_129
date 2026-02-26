edad = int(input("¿Cuántos años tienes? "))
name = input("¿Cuál es tu nombre? ")

if edad >= 18 and (name == "Juan" or name == "Lourdes"):
  print("Eres mayor de edad")
elif edad == 17:
  print("Te falta poco")
else:
  print("Eres menor de edad")