from flask import render_template
from flask import request
from flask import jsonify
import json
from app import app
from app.models import User


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data.decode())
    username = data['username']
    password = data['password']
    user = User()

    was_added = user.add(username, password)

    return jsonify(was_added=was_added), 200

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = json.loads(request.data.decode())
    weight = float(data['weight'])
    height = float(data['height']) / 100
    bmi = weight / (height * height)

    return jsonify(bmi=round(bmi, 2)), 200
