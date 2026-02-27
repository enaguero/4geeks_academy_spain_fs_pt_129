from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.errorhandler(400)
def handle_bad_request(error):
    message = getattr(error, "description", "Request invalida")
    return jsonify({"detail": message}), 400


def parse_int_query(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = request.args.get(name)
    if raw is None:
        return default

    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"{name} debe ser un entero")

    if value < minimum or value > maximum:
        raise ValueError(f"{name} debe estar entre {minimum} y {maximum}")

    return value


def parse_bool_query(name: str, default: bool) -> bool:
    raw = request.args.get(name)
    if raw is None:
        return default

    value = raw.strip().lower()
    if value in {"true", "1", "yes"}:
        return True
    if value in {"false", "0", "no"}:
        return False

    raise ValueError(f"{name} debe ser true o false")


@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    return jsonify({"user_id": user_id, "message": "Detalle de usuario"})


@app.get("/products")
def list_products():
    try:
        limit = parse_int_query("limit", default=10, minimum=1, maximum=100)
        active = parse_bool_query("active", default=True)
    except ValueError as exc:
        return jsonify({"detail": str(exc)}), 400

    category = request.args.get("category")
    return jsonify(
        {
            "limit": limit,
            "active": active,
            "category": category,
            "message": "Listado de productos con filtros",
        }
    )


@app.get("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"detail": "q es requerido"}), 400
    if len(query) > 50:
        return jsonify({"detail": "q no puede superar 50 caracteres"}), 400

    return jsonify({"query": query, "message": "Resultados de busqueda"})


if __name__ == "__main__":
    app.run(debug=True)
