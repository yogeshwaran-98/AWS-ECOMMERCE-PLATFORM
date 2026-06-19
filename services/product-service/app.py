from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "product-service",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop",
            "price": 75000
        },
        {
            "id": 2,
            "name": "Phone",
            "price": 25000
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)