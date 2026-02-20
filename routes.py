
from flask import request, jsonify
import app
from users import create_user
from users import login_user


@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    result = create_user(data["email"], data["password"])
    return jsonify(result)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    result = login_user(data["email"], data["password"])
    return jsonify(result)
