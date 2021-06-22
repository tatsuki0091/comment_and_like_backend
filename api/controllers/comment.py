from flask import Flask, request, Blueprint, jsonify
from api.models import Comment, CommentSchema

# To call method in this class
handleComment = Blueprint('comment', __name__, url_prefix='/')

@handleComment.route('/api/comment', methods=['POST', 'GET'])
def comment():
    if request.method == 'POST':
        # Register a comment
        comment_result = Comment.registerComment(request.json)
        res = {
            'code': 200,
            'user_id': comment_result.user_id,
            'text': comment_result.text,
        }
        return jsonify(res), 200
    else:
        # Select cpmments
        results = Comment.query.all()
        res = {
            'code': 200,
            'comments': CommentSchema(many=True).dump(results)
        }

        return jsonify(res), 200

