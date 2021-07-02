from datetime import datetime
from api.database import db, ma

class Like(db.Model):

    # Define Table name
    __tablename__ = 'likes'

    # Define column of table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'),  nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id, comment_id):
        self.user_id = user_id
        self.comment_id = comment_id

    def registerLike(like):
        record = Like(
            user_id=like['user_id'],
            comment_id=like['comment_id'],
        )

        try:
            db.session.add(record)
            db.session.commit()
            return record
        except Exception as e:
            return e

    def deleteLike(like):
        try:
            db.session.delete(like)
            db.session.commit()
            return like
        except Exception as e:
            return e

class LikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Apporopriate model properties for all schima
        model = Like
        fields = ("id", "user_id", "comment_id")