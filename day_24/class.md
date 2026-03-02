# Programación Orientada a Objetos

## Problema

```python

data = { "name": "Andres", "lastName": "Erwin"}
data["name"] -> "Andres"
```

```python
members = []
next_id = 1

def create_member(data):
    global next_id
    # Validación repetida (aparecerá también en update_member)
    if "first_name" not in data or data["first_Name"] == "":
        return {"error": "first_name is required"}, 400
    if "age" not in data or data["age"] < 0:
        return {"error": "invalid age"}, 400

    member = {
        "id": next_id,
        "first_name": data["firstname"],
        "age": data["age"],
        "lucky_numbers": data.get("lucky_numbers", []),
    }
    members.append(member)
    next_id += 1
    return member, 201

def update_member(member_id, data):
    for m in members:
        if m["id"] == member_id:
            # Repetición de validación (misma regla en otro sitio)
            if "age" in data and data["age"] < 0:
                return {"error": "invalid age"}, 400

            # Error típico de clave inconsistente:
            # aquí alguien escribió "firstname" en vez de "first_name"
            if "firstname" in data:
                m["firstname"] = data["firstname"]

            if "first_name" in data:
                m["first_name"] = data["first_name"]
            return m, 200
    return {"error": "member not found"}, 404
```

## Idea

Carro : model, año, marca, color

```python

class Car:
  def __init__(self, model, year, brand, color):
    self.model = model
    self.year = year
    self.brand = brand
    self.color = color
    self.distance = 0

  def travel(a, b):
    self.distance += (b - a)
```

## Elemento en concreto de esa idea

```python
car_one = Car("super fast", "2026", "Mercedez", "silver")

car_two = Car("fast", "2020", "Kia", "red")
```
