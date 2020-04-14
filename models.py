"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG = 'data:image/png;base64,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'

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, default=DEFAULT_IMG, nullable=False)
    
    # @property Helped fix '<bound method User.full_name of <User 3>>'
    @property
    def full_name(self):
        """Return first & last name"""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='post')

    @property
    def formated_date(self):
        """Formats the date for users"""

        return self.created_at.strftime("%b %d %Y %H:%M:%S")

class PostTag(db.Model):
    __tablename__ = 'post_tag'

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)

class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    # form a relationship between tag & post, with a secondary of our intersection table
    post = db.relationship('Post', secondary='post_tag', backref='tag')
