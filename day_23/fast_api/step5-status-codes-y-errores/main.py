from typing import Dict

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Step 5 - Status codes y errores")


class OrderCreate(BaseModel):
    customer: str = Field(min_length=2, max_length=60)
    total: float = Field(gt=0)


orders: Dict[int, Dict[str, object]] = {
    1: {"id": 1, "customer": "Ana", "total": 22.5},
    2: {"id": 2, "customer": "Leo", "total": 13.0},
}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido no encontrado")
    return order


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate):
    next_id = max(orders.keys(), default=0) + 1
    if any(order["customer"] == payload.customer for order in orders.values()):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un pedido para ese cliente",
        )

    order = {"id": next_id, "customer": payload.customer, "total": payload.total}
    orders[next_id] = order
    return order


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int):
    if order_id not in orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido no encontrado")

    del orders[order_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
