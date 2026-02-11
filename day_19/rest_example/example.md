# API Rest

1. HTTP permite transferir informacion entre computadores
2. HTTP usa una interfaz (API) para saber que informacion debe enviar.
3. HTTP usa un keyword (palabra especial) para indicar que accion hacer:

- obtener informacion : GET (yo no envio informacion)
- crear informacion : POST
- Actualizar una informacion de modo completo: PUT
- Actualizar una informacion de modo parcial : PATCH
- Borrar informacion : DELETE

4. ¿Que formato tiene la informacion?

Ejemplo GET Plural
REST: Representational State Transfer -> JSON (JavaScript Object Notation)

resource: `cars`, `people`, `animals`, `laptos`

Obtener varios autos

base : http://my-super-api.com/v1/

end-point : /<resource>

HTTP : GET

```
{
  "data": [
    {
      "uuid": "123423",
      "brand": "ford",
      "model": "cachilupi-ford-fiesta"
    },
    {
      "uuid": "123427",
      "brand": "citroen",
      "model": "cachilupi-citroen-fiesta"
    },
    ....
  ]
}

```

- GET Singular de un recurso

base : http://my-super-api.com/v1/
end-point : /<resource>/:id

ejemeplo: http://my-super-api.com/v1/cars/123427

```
{
  "data":  {
      "uuid": "123427",
      "brand": "citroen",
      "model": "cachilupi-citroen-fiesta"
    }
}
```
