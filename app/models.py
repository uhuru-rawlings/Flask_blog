from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db


@login_manager.user_loader 
def load_user(user_id):
     return registration.query.get(int(user_id))

class registration(db.Model, UserMixin):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    useremail = db.Column(db.String(100))
    password = db.Column(db.String(300))


    def __repr__(self):
        return f'(self.username)'

class blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.String(3999))
    postby = db.Column(db.String(100))
    blog_image = db.Column(db.String(150))
    blog_title = db.Column(db.String(150))
    blog_pitch = db.Column(db.String(1000))

class coments(db.Model):
    __tablename__ = 'coments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(200))


class contacts(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key = True)
    phone = db.Column(db.Integer)
    useremail = db.Column(db.String(200))
    message = db.Column(db.String(1000))

class newslater(db.Model):
    __tablename__ = 'newslater'
    id = db.Column(db.Integer, primary_key = True)
    useremail = db.Column(db.String(200))

class Quotes():
    def __init__(self, author,quote):
       self.author = author
       self.quote = quote
