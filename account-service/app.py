from flask import Flask, jsonify

app = Flask(__name__)

accounts = [
    {"id": 1, "customer_id": 1, "balance": 5000.00},
    {"id": 2, "customer_id": 2, "balance": 3000.00}
]

@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify(accounts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

