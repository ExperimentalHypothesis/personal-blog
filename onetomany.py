from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///onetomany.db"
db = SQLAlchemy(app)

class AlbumModel(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    songs = db.relationship("SongModel")

class SongModel(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    album = db.relationship("AlbumModel")
