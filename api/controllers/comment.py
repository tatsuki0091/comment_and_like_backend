from flask import Flask, request, Blueprint, jsonify
from api.models import Comment, CommentSchema
from api.models import Like

# To call method in this class
handleGetComment = Blueprint('getCcomment', __name__, url_prefix='/')
handlePostComment = Blueprint('postComment', __name__, url_prefix='/')


@handlePostComment.route('/api/post_comment', methods=['POST'])
def postComment():
    # Register a comment
    comment_result = Comment.registerComment(request.json)
    commentInfo = Comment.query.filter((Comment.user_id == comment_result.user_id) & (
            Comment.text == comment_result.text)).first()
    print(commentInfo)
    return jsonify(CommentSchema().dump(commentInfo)), 200

@handleGetComment.route('/api/get_comment/<user_id>', methods=['GET'])
def getCcomment(user_id):
    # Select cpmments
    # results = Comment.query.all()
    results = Comment.selectCommentsAndLikes(self=None)
    likeEesults = Like.query.filter((Like.user_id == user_id)).order_by(Like.comment_id).all()
    array = []
    for result in results:
        dic = {
            'id': result[0].id,
            'user_id': result[0].user_id,
            'text': result[0].text,
            'created_at': result[0].created_at,
            'updated_at': result[0].updated_at,
            'count': result[1],
        }
        for likeEesult in likeEesults:
            if likeEesult.user_id == result[0].user_id and likeEesult.comment_id == result[0].id:
                dic['liked'] = True
        if 'liked' not in dic:
            dic['liked'] = False
        array.append(dic)
    # return comments
    return jsonify(array), 200


