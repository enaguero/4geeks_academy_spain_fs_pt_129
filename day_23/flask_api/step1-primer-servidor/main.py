from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.get("/")
def root():
    return jsonify({"message": "API viva y respondiendo"})


@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/saludo")
def saludo():
    return jsonify({"message": "Hola! Bienvenido a tu primera API con Flask"})


if __name__ == "__main__":
    app.run(debug=True)
