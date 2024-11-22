from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/customers', methods=['GET'])
def get_customers():
    response = requests.get('http://customer-service:5001/customers')
    return jsonify(response.json())

@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    response = requests.get('http://account-service:5002/accounts')
    return jsonify(response.json())

@app.route('/api/transactions', methods=['GET', 'POST'])
def handle_transactions():
    if request.method == 'GET':
        response = requests.get('http://transaction-service:5003/transactions')
        return jsonify(response.json())
    elif request.method == 'POST':
        response = requests.post('http://transaction-service:5003/transactions', json=request.json)
        return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

