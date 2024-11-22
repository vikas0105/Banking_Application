from flask import Flask, jsonify

app = Flask(__name__)

customers = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

