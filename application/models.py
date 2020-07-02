from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    """ Must have callback function as decribed in the docs: https://flask-login.readthedocs.io/en/latest/ """
    return AdminModel.query.get(int(id))


class MessageModel(db.Model):
    """ Data model for message from contact form """

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    email = db.Column(db.String(64), unique=False, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    time_sent = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"<Message {self.id}, {self.name}>"


class PostModel(db.Model):
    """ Data model for post """

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    tags = db.Column(db.Text, unique=False, nullable=True)
    time_posted = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"


class ProjectModel(db.Model):
    """ Data model for project """

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    project_url = db.Column(db.String(256), unique=False, nullable=True)
    github_url = db.Column(db.String(256), unique=False, nullable=True)
    time_added = db.Column(db.DateTime, unique=False, nullable=False)
    
    def __repr__(self):
        return f"<Project {self.id}: {self.title}>"


class AdminModel(db.Model, UserMixin):
    """ Data model for admin """

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<Admin {self.email}>"


