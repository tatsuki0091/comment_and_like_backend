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
            'user_id': comment_result.user_id,
            'text': comment_result.text,
        }
        return res, 200
    else:
        # Select cpmments
        results = Comment.query.all()
        # return comments
        return jsonify(CommentSchema(many=True).dump(results)), 200

