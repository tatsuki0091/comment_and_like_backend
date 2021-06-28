from datetime import datetime
from api.database import db, ma
from .like import Like
from sqlalchemy import func

class Comment(db.Model):

    # Define Table name
    __tablename__ = 'comments'

    # Define column of table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String(250),  nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    like = db.relationship(Like, backref='comments', uselist=False)

    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def registerComment(comment):
        record = Comment(
            user_id=comment['user_id'],
            text=comment['text'],
        )
        try:
            db.session.add(record)
            db.session.commit()
            return record
        except Exception as e:
            return e

    def selectCommentsAndLikes(self):
        results = db.session.query(Comment, func.count(Like.comment_id))\
            .outerjoin(Like, Comment.id == Like.comment_id).group_by(Comment.id).order_by(Comment.id).all()
        return results


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Apporopriate model properties for all schima
        model = Comment

        fields = ("id", "user_id", "text", "created_at", "updated_at")

