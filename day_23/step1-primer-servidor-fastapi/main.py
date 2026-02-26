from fastapi import FastAPI

app = FastAPI(
    title="Step 1 - Primer servidor FastAPI",
    description="Endpoints basicos para confirmar que la API esta funcionando.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "API viva y respondiendo"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/saludo")
def saludo():
    return {"message": "Hola! Bienvenido a tu primera API con FastAPI"}
