from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    Class to create new users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    # Relationship with the Blog Post table 
    posts = db.relationship('Blog', backref = 'author', lazy = "dynamic")
    # Relationship with the Comments table
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    '''
    Class to create roles for our new users
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
    
class Quote:
    def __init__(self,id, author, quote, permalink):
        self.id = id
        self.author = author 
        self.quote  = quote
        self.permalink =  permalink

class Blog(db.Model):
    __tablename__ = "blogs"
    '''
    Class for blog posts
    '''
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable = False)
    posted = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)

    # Relationship with the user table
    users = db.relationship(User)
    
    # Relationship with the Comments table 
    comments = db.relationship('Comment', backref='blogs', lazy='dynamic')
    
    def __repr__(self):
        return f"POST ID:{self.id} -- Date: {self.posted}"  

class Comment(db.Model):
    '''
    Class for the comment section
    '''

    __tablename__='comments'

    id  = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()
    
    @classmethod
    def delete_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()

        return comments