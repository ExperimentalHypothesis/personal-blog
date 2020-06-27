from application import db

class MessageModel(db.Model):
    """ Data model for message from contact form """

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    email = db.Column(db.String(64), unique=False, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    time_sent = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"<MessageModel {self.id}, {self.name}>"


class PostModel(db.Model):
    """ Data model for new post """

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    tags = db.Column(db.Text, unique=False, nullable=True)
    time_posted = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"<PostModel {self.id}, {self.title}>"



