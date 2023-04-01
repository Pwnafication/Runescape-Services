from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm
from functools import wraps
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return UserTable.query.get(int(user_id))

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("UserTable", back_populates="posts")
    author_id = db.Column(db.Integer, db.ForeignKey("User_Table.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="blog_post")

class UserTable(UserMixin, db.Model):
    __tablename__ = "User_Table"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(750), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("User_Table.id"))
    comment_author = relationship("UserTable", back_populates="comments")
    blogpost_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    blog_post = relationship("BlogPost", back_populates="comments")