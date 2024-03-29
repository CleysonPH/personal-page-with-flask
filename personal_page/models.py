from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import date

from personal_page import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    description = db.Column(db.Text, nullable=False, default='Meu nome é Fulaninho e eu gosto de fulanizar')
    image = db.Column(db.String(120), nullable=False, default='https://cleysonph.github.io/imagens/perfil.jpg')


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)


    def __repr__(self):
        return '<User> username: {}'.format(self.username)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(120), nullable=False, default='https://placekitten.com/500/300')
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    certification_link = db.Column(db.String(120), nullable=False)
    conclusion_date = db.Column(db.Date)
