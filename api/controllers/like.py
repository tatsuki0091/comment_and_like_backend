from flask import Flask, request, Blueprint, jsonify
from api.models import Like, LikeSchema

handleLike = Blueprint('like', __name__, url_prefix='/')
handleIsFavorite = Blueprint('is_favorite', __name__, url_prefix='/')
handleLikeCount= Blueprint('like_count', __name__, url_prefix='/')

@handleLike.route('/api/like', methods=['POST', 'GET', 'DELETE'])
def like():
    if request.method == 'POST':
        # Register a comment
        like_result = Like.registerLike(request.json)
        # likeInfo = Like.query.filter((Like.user_id == like_result.user_id) & (
        #             Like.comment_id == like_result.comment_id)).first()
        res = {
            'user_id': like_result.user_id,
            'comment_id': like_result.comment_id,
        }
        return res, 200
    elif request.method == 'DELETE':
        # Get like infor
        likeInfo = Like.query.filter((Like.user_id == request.json['like']['user_id']) & (Like.comment_id == request.json['like']['comment_id'])).first()

        # Delete like info
        result = Like.deleteLike(likeInfo)

        return jsonify(LikeSchema().dump(result)), 200
    else:
        # res = {
        #     'user_id': like_result.user_id,
        #     'comment_id': like_result.comment_id,
        # }
        return "ddd", 200

@handleIsFavorite.route('/api/is_favorite/<user_id>/<comment_id>', methods=['GET'])
# @handleIsFavorite.route('/<user_id>/<comment_id>')
def like(user_id, comment_id):
    # Get like info
    result = Like.query.filter((Like.user_id == user_id) & (Like.comment_id == comment_id)).first()
    return jsonify(LikeSchema().dump(result)), 200

@handleLikeCount.route('/api/count_like', methods=['GET'])
def countLike():
    results = Like.countLike(self=None)
    res = []
    for id, count in results:
        dic = {
            'comment_id': id,
            'count': count,
        }
        res.append(dic)
    return jsonify(res), 200