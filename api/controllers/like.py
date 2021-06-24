from flask import Flask, request, Blueprint, jsonify
from api.models import Like

handleLike = Blueprint('like', __name__, url_prefix='/')

@handleLike.route('/api/like', methods=['POST', 'GET', 'DELETE'])
def like():
    if request.method == 'POST':
        # Register a comment
        comment_result = Like.registerComment(request.json)
        res = {
            'user_id': comment_result.user_id,
            'text': comment_result.text,
        }
        return res, 200