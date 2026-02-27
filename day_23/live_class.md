# Crear tu primera API

- Crear los end-points (o crear las urls) que un servidor "expone".
- Llama a la documentación que hemos visto en contact list, start wards, etc.
- API : Application Programming Interface.

1. Nos encontramos en un ciclo circular: clienta llama a servidor y servidor responde a cliente.
2. Cliente ocupa un protocolo: HTTP/HTTPS
3. Métodos de comunicación del protocolo: GET, POST, PATCH, PUT, DELETE.
   3.1 -> PATCH : Actualización parcial*
   3.2 -> PUT : Actualización completa*
4. REST : Una forma de diseño de urls en una API para crear un "recurso" o concepto donde se ejecuta los diferentes metodos del protocolo de comunicación.

4.1 - Identificación del recurso: Se refiere a un sustantivo : "users", "products", "cars".
4.2 - Asociación del método de comunicación del protocolo al sustantivo.

- Recuperar todos los elementos del recurso: "GET /users"

```
response: 200

[
  {
      uuid: "absd2-123tr-quwquqw4",
      name: "Andres",
      lastName: "Meza",
      dateOfBirth: "01/12/1985",
      email: "student@4geeks.com"
  },
    {
      uuid: "absd2-123tr-quwquqw4",
      name: "Andres",
      lastName: "Meza",
      dateOfBirth: "01/12/1985",
      email: "student@4geeks.com"
  }
]

```

- Recuperar solo un elemenot del recurso : "GET /users/:userId" (vista detalle -> elemento específico)

```
GET /users/absd2-123tr-quwquqw4

{
  uuid: "absd2-123tr-quwquqw4",
  name: "Andres",
  lastName: "Meza",
  dateOfBirth: "01/12/1985",
  email: "student@4geeks.com"
}

```

- Actualizar de modo parcial el recurso con PATCH:

```

PATCH /users/:userId

request (body): JSON

{
  dateOfBirth: "12/12/1985" -> Envio solo un campo (actualización parcial)
}

```

- Actualizar el recurso de modo completo con PUT:

Ejemplo erroneo:

```

PUT /users/:userId

request (body): JSON

{
  dateOfBirth: "12/12/1985" -> Envio solo un campo (actualización parcial) -> servidor te responde un 4XX
}

fetch("https://dominio.com/users/:userId", {
  METHOD: "PUT",
  BODY: {
    dateOfBirth: "12/12/1985"
  }
}).then((res) => res.status)
.then(()=> )
.catch(()=> {

})

```

El ejemplo completo es cuando se envia toda la información (todos los campos):

```
PUT /users/:userId

{
  name: "Andres",
  lastName: "Meza",
  dateOfBirth: "12/12/1985",
  email: "student_senior@4geeks.com"
}
```

- Delete: Borrar un recursor:

```
DELETE /users/:userId
```

## Anidación

```
METHOD /resources/:resourceId/nestedResources/
```

```
GET /products

body:
[
  {
    uuid: "123iqweqw-12312niadsa",
    name: "perfume-abc",
    brand: "morning",
    model: "winter"
  }
]

GET /products/123iqweqw-12312niadsa

  {
    name: "perfume-abc",
    brand: "morning",
    model: "winter"
  }

GET /users/:userId/products

GET /users/absd2-123tr-quwquqw4
```
