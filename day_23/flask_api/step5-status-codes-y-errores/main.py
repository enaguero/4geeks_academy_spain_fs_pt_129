from typing import Dict

from flask import Flask, jsonify, request
from pydantic import BaseModel, Field, ValidationError

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


class OrderCreate(BaseModel):
    customer: str = Field(min_length=2, max_length=60)
    total: float = Field(gt=0)


orders: Dict[int, Dict[str, object]] = {
    1: {"id": 1, "customer": "Ana", "total": 22.5},
    2: {"id": 2, "customer": "Leo", "total": 13.0},
}


def parse_payload(model_cls):
    payload = request.get_json(silent=True)
    if payload is None:
        return None, jsonify({"detail": "Body JSON requerido"}), 400

    try:
        return model_cls(**payload), None, None
    except ValidationError as exc:
        return None, jsonify({"detail": exc.errors()}), 422


@app.get("/orders/<int:order_id>")
def get_order(order_id: int):
    order = orders.get(order_id)
    if order is None:
        return jsonify({"detail": "Pedido no encontrado"}), 404
    return jsonify(order)


@app.post("/orders")
def create_order():
    payload, error_response, status_code = parse_payload(OrderCreate)
    if error_response is not None:
        return error_response, status_code

    if any(order["customer"] == payload.customer for order in orders.values()):
        return jsonify({"detail": "Ya existe un pedido para ese cliente"}), 409

    next_id = max(orders.keys(), default=0) + 1
    order = {"id": next_id, "customer": payload.customer, "total": payload.total}
    orders[next_id] = order
    return jsonify(order), 201


@app.delete("/orders/<int:order_id>")
def delete_order(order_id: int):
    if order_id not in orders:
        return jsonify({"detail": "Pedido no encontrado"}), 404

    del orders[order_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
