
# Definicion de variables
name = "Erwin"
age = 30
data = None

print(data)

# Datos basicos
nombre = "Carlos"      # str
edad = 31               # int
altura = 1.78           # float
es_estudiante = True    # bool
person = {
    "nombre": "Carlos", 
    "edad": 31,
    "saldo_cuenta": 100.50,
    "profesion": "Ingeniero"
  }  # dict


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Andres", 25)

print(p)
print(p.name)

print(type(nombre))
print(type(edad))
print(type(person))


country = input("¿En que pais te encuentras? ")
print(type(country))
print("Tu pais es: " + country)


age = input("¿Cuantos años tienes? ")
print(type(age))

print(type(int(age)))

parsed_age = int(age)
print("Tu edad es: " + str(10 + parsed_age))



