from flask import Flask, Response, request, Blueprint, jsonify
from api.models import Comment, CommentSchema

# To call method in this class
comment = Blueprint('comment', __name__, url_prefix='/')

@comment.route('/api/comment', methods=['POST', 'GET'])
def postComment():
    if request.method == 'POST':
        comment_result = Comment.registerComment(request.json)
        print(comment_result)
        res = {
            'code': 200,
            'user_id': comment_result.user_id,
            'text': comment_result.text,
        }
        return jsonify(res), 200
    else:
        res = {
            'message': 'get'
        }

        return jsonify(res), 200

