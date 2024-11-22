from flask import Flask, request, jsonify

app = Flask(__name__)

transactions = []

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transactions.append(data)
    return jsonify({"message": "Transaction recorded!", "transaction": data}), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

