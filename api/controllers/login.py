import json
import os
import time
from flask import Flask, Response, request, Blueprint, jsonify

# To call method in this class
loginAuth = Blueprint('login', __name__, url_prefix='/')

@loginAuth.route('/', methods=['GET'])
def login():

    res = {
        'message': 'rootです'
    }

    return jsonify(res), 200