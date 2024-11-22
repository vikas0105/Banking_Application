from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    if username:
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Username is required'}), 400

@app.route('/auth/verify', methods=['POST'])
def verify():
    token = request.json.get("token")
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({'status': 'valid', 'user': decoded['user']}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

