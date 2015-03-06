#not all of these imports used
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db#,oid, lm
from .forms import LoginForm
from .models import User

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
							title='Sign In',
							form=form)

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} #fake user
	db_user = User.query.filter_by(nickname=user['nickname']).first()
	posts = db_user.posts.all()
	
	"""
	Generic form of a posts array, will work.
	posts = [
		{ 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
	]
	"""
	
	return render_template('index.html',
							title='Home',
							user=user,
							#user={'nickname':''},
							posts=posts)
	
@app.route('/seven')
def ret_seven():
	return "7?"