from flask import Flask, Response, request, Blueprint, jsonify

# To call method in this class
comment = Blueprint('comment', __name__, url_prefix='/')

@comment.route('/api/comment', methods=['POST', 'GET'])
def postComment():
    if request.method == 'POST':
        res = {
            'message': 'post'
        }

        return jsonify(res), 200
    else:
        res = {
            'message': 'get'
        }

        return jsonify(res), 200

