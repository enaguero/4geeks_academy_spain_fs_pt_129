
def saludar(message):
  print(f"Hola, {message}!")

saludar("Mundo , Ruben!!!")

def sumar(a, b):
  return a + b

resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")

def saludar_multilingue(nombre, idioma="es"):
    if idioma == "es":
        return f"Hola {nombre}"
    if idioma == "en":
        return f"Hello {nombre}"
    return f"Saludo no disponible para {nombre}"

print(saludar_multilingue("Andres"))
print(saludar_multilingue("Andres", "en"))
print(saludar_multilingue("Andres", "fr"))