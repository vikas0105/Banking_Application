from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notifications/send', methods=['POST'])
def send_notification():
    data = request.json
    user = data.get("user")
    message = data.get("message")
    # Simulate notification logic
    return jsonify({"status": "success", "user": user, "message": message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)

