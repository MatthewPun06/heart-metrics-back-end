import os
from flask import Flask, request, jsonify
from sb_client import supabase
from users import create_user, login_user
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# routes

@app.route("/api/index", methods=["GET"])
def index():   
    try:
        response = supabase.table('users').select("*").execute()
        return jsonify(response.data if response.data else [])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.json
    result = create_user(data["name"], data["email"], data["password"])
    print(result)
    return jsonify(result)

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    result = login_user(data["email"], data["password"])
    return jsonify(result)

@app.route("/api/delete/<user_id>", methods=["GET"])
def delete_user(user_id: str):
    result = delete_user(user_id)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug=True)