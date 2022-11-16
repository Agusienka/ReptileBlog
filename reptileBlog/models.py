from datetime import datetime
from flask_login import UserMixin
from reptileBlog import db, login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(250), nullable=False)
    scientific_name = db.Column(db.String(250), nullable=False)
    conservation_status = db.Column(db.String(500), nullable=False)
    native_habitat = db.Column(db.String(500), nullable=False)
    fun_fact = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.common_name}', '{self.scientific_name}', '{self.conservation_status}', '{self.native_habitat}', '{self.fun_fact}', '{self.image}', '{self.date_posted}')"

