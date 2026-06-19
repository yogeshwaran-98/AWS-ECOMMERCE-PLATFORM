from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/orders")
def orders():
    return jsonify([
        {
            "id": 1001,
            "user": 1,
            "status": "CREATED"
        },
        {
            "id": 1002,
            "user": 2,
            "status": "SHIPPED"
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)