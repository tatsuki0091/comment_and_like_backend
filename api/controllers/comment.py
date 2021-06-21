from flask import Flask, Response, request, Blueprint, jsonify

# To call method in this class
postComment = Blueprint('comment', __name__, url_prefix='/')

@postComment.route('/', methods=['POST'])
def postComment():

    res = {
        'message': 'comment'
    }

    return jsonify(res), 200