from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simulated transaction data
TRANSACTION_DATA = [
    {"id": 1, "account": "123456789", "amount": 500, "type": "credit"},
    {"id": 2, "account": "987654321", "amount": 200, "type": "debit"},
    {"id": 3, "account": "123456789", "amount": 150, "type": "debit"},
]

@app.route('/analytics/report', methods=['GET'])
def generate_report():
    # Generate a simple summary report
    total_credits = sum(txn["amount"] for txn in TRANSACTION_DATA if txn["type"] == "credit")
    total_debits = sum(txn["amount"] for txn in TRANSACTION_DATA if txn["type"] == "debit")
    return jsonify({
        "total_transactions": len(TRANSACTION_DATA),
        "total_credits": total_credits,
        "total_debits": total_debits,
        "net_balance": total_credits - total_debits
    }), 200

@app.route('/analytics/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transaction_id = random.randint(100, 999)
    TRANSACTION_DATA.append({
        "id": transaction_id,
        "account": data.get("account"),
        "amount": data.get("amount"),
        "type": data.get("type"),
    })
    return jsonify({"status": "success", "transaction_id": transaction_id}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)

