import json
import os
import time
from flask import Flask, Response, request, Blueprint, jsonify
from api.models.user import User

# To call method in this class
loginAuth = Blueprint('login', __name__, url_prefix='/')

@loginAuth.route('/api/login', methods=['POST'])
def login():
    # Get user info from request
    email = request.json['email']
    password = request.json['password']

    # Select user info
    result = User.query.filter((User.email == email) & (User.password == password)).first()
    # Set email address to return
    if result is not None:
        res = {
            'id': result.id,
            'email': result.email
        }
    else:
        res = {}

    # return email address as a JASON
    return jsonify(res), 200