from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI(title="Step 2 - Rutas y parametros")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": "Detalle de usuario"}


@app.get("/products")
def list_products(
    limit: int = Query(default=10, ge=1, le=100),
    active: bool = True,
    category: Optional[str] = None,
):
    return {
        "limit": limit,
        "active": active,
        "category": category,
        "message": "Listado de productos con filtros",
    }


@app.get("/search")
def search(q: str = Query(min_length=1, max_length=50)):
    return {"query": q, "message": "Resultados de busqueda"}
