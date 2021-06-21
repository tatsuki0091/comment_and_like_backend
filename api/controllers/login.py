import json
import os
import time
from flask import Flask, Response, request, Blueprint, jsonify
from api.models.user import User

# To call method in this class
loginAuth = Blueprint('login', __name__, url_prefix='/')

@loginAuth.route('/api/login', methods=['POST'])
def login():
    data = request.data.decode('utf-8')
    email = request.json['email']
    password = request.json['password']
    result = User.query.filter((User.email == email) | (User.password == password)).all()
    print(result)

    res = {
        'message': 'rootです'
    }

    return jsonify(res), 200