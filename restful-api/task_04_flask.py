from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Return all usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Dynamic user endpoint
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# Add user endpoint
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()