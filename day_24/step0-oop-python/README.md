🇪🇸 **Español** | [🇬🇧 English](README.en.md)

# 🧭 Step 0: OOP en Python (Incremental)

## 🎯 Objetivo

Entender desde cero:

1. Qué problema resuelve la Programación Orientada a Objetos (OOP).
2. Qué es una `class`.
3. Qué es un `object`.
4. Qué es un `attribute`.
5. Qué es un `method`.

Al final, estarás listo para modelar la base de la **Family Static API**.

---

## 1) ¿Qué problema resuelve OOP?

Cuando empezamos, solemos hacer una API en memoria con listas + diccionarios + funciones sueltas:

```python
members = []
next_id = 1

def create_member(data):
    global next_id
    # Validación repetida (aparecerá también en update_member)
    if "first_name" not in data or data["first_name"] == "":
        return {"error": "first_name is required"}, 400
    if "age" not in data or data["age"] < 0:
        return {"error": "invalid age"}, 400

    member = {
        "id": next_id,
        "first_name": data["first_name"],
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

Este enfoque funciona al principio, pero cuando crece el proyecto aparecen problemas reales:

- **Reglas duplicadas**: validaciones repetidas entre `create_member`, `update_member`, etc.
- **Errores de consistencia**: se mezclan claves (`"firstname"` y `"first_name"`), rompiendo respuestas.
- **Mantenimiento difícil**: si cambias una regla (por ejemplo edad mínima), debes buscar y editar muchas funciones.

OOP ayuda a organizar mejor:

- Junta **datos + comportamiento** en una misma unidad.
- Te permite modelar entidades reales (`Family`, `Member`).
- Hace el código más mantenible al crecer.

---

## 2) ¿Qué es una `class`?

Una `class` es una **plantilla**.  
Define cómo serán los objetos que se creen desde ella.

Piensa en ella como un “molde”.

```python
class Dog:
    pass
```

Aquí `Dog` es la plantilla, pero todavía no hay ningún perro real.

### Mini ejercicio 1

1. Crea una clase llamada `Car`.
2. Crea una clase llamada `Student`.
3. Ejecuta el archivo y verifica que no da error.

---

## 3) ¿Qué es un `object`?

Un `object` (objeto) es una **instancia concreta** de una clase.

```python
class Dog:
    pass

dog_1 = Dog()
dog_2 = Dog()

print(type(dog_1))  # <class '__main__.Dog'>
print(dog_1 == dog_2)  # False
```

Aunque ambos vienen de la misma clase, son objetos distintos.

### Mini ejercicio 2

1. Crea `car_1 = Car()` y `car_2 = Car()`.
2. Imprime `type(car_1)`.
3. Compara `car_1 == car_2`.

---

## 4) ¿Qué es un `attribute`?

Un atributo es un dato que vive dentro del objeto.

Para inicializar atributos usamos normalmente `__init__`:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog_1 = Dog("Toby", 4)
print(dog_1.name)  # Toby
print(dog_1.age)   # 4
```

Claves:

- `self` representa el objeto actual.
- `self.name` y `self.age` son atributos del objeto.

### Mini ejercicio 3

1. Define clase `Student` con atributos `name` y `cohort`.
2. Crea un objeto `student_1`.
3. Imprime sus atributos.

---

## 5) ¿Qué es un `method`?

Un método es una función definida dentro de la clase.

Sirve para expresar comportamiento del objeto.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: woof!"

    def birthday(self):
        self.age += 1

dog_1 = Dog("Toby", 4)
print(dog_1.bark())   # Toby says: woof!
dog_1.birthday()
print(dog_1.age)      # 5
```

`bark` y `birthday` son métodos.  
`birthday` modifica el estado del objeto (`age`).

### Mini ejercicio 4

1. En `Student`, crea método `introduce()` que retorne un texto.
2. Crea método `change_cohort(new_cohort)` para actualizar el atributo.
3. Ejecuta y valida que el cambio se refleje.

---

## 6) Todo junto: modelo simple para Family API

En este día, nuestro dominio es una familia y sus miembros.

```python
class Member:
    def __init__(self, member_id, first_name, age):
        self.id = member_id
        self.first_name = first_name
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
        }
```

Mapeo mental:

- `class Member` -> plantilla
- `member = Member(...)` -> objeto concreto
- `self.first_name` -> atributo
- `to_dict()` -> método

Esto encaja directo con Flask:

- Flask recibe request HTTP
- Tu clase aplica reglas
- Flask devuelve JSON con `to_dict()`

---

## 7) Práctica guiada del step

Usa el archivo [`oop_examples.py`](./oop_examples.py):

```bash
python day_24/step0-oop-python/oop_examples.py
```

Qué observar:

- `Member` encapsula los datos de un miembro.
- `Family` encapsula operaciones del grupo (`add_member`, `get_member`, `delete_member`).
- `get_all_members()` transforma objetos a diccionarios para exponer JSON.

---

## 8) Mini retos de validación final

1. Agrega atributo `hobby` a `Member` y refléjalo en `to_dict`.
2. Crea método `is_adult()` que retorne `True` si `age >= 18`.
3. Evita crear miembros con edad negativa.
4. En `Family`, crea método `update_member_name(member_id, new_name)`.
5. Prueba caso feliz y caso de error en cada método.

---

## ✅ Checklist de aprendizaje

- [ ] Puedo explicar qué problema resuelve OOP.
- [ ] Puedo definir con mis palabras `class`, `object`, `attribute`, `method`.
- [ ] Puedo crear una clase con `__init__`.
- [ ] Puedo crear objetos y llamar métodos.
- [ ] Puedo conectar este modelo mental con una API Flask.

---

## 📖 Lectura oficial de este step

- [What is Object Oriented Programming?](https://4geeks.com/syllabus/spain-fs-pt-129/read/oop-in-python)
