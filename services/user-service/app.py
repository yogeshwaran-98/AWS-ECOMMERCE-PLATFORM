from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/users")
def get_users():
    return jsonify([
        {
            "id": 1,
            "name": "Alice"
        },
        {
            "id": 2,
            "name": "Bob"
        },
        {
            "id": 3,
            "name": "Charlie"
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3000
    )