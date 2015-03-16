#not all of these imports used
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db#,oid, lm
from .forms import LoginForm, NewTripForm
from .models import User
from .models import Trip

@app.route('/newtrip', methods=['GET','POST'])
def newtrip():
	form = NewTripForm()
	# Validation now just ensures no fields are empty, should check that times are valid
	if form.validate_on_submit():
		flash("Received trip from %s to %s" % (form.destination.data, form.origin.data))
		t = Trip(origin=form.origin.data,
				destination=form.destination.data,
				contact_info=form.contact.data,
				date=form.day.data,
				TOA=form.arrival_time.data,
				TOD=form.depart_time.data)
		db.session.add(t)
		db.session.commit()
		return redirect('/index') # if successful post, return to home page
	
	return render_template('newtrip.html',
							title='Post a new trip',
							form=form
							)

@app.route('/')
@app.route('/index')
def index():
	
	trips = Trip.query.all()
	
	return render_template('index.html',
							title='Home',
							trips=trips)
	
	
	
	#user = {'nickname': 'Miguel'} #fake user
	#db_user = User.query.filter_by(nickname=user['nickname']).first()
	#posts = db_user.posts.all()
	
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
	#return render_template('index.html',
	#						title='Home',
	#						user=user,
	#						#user={'nickname':''},
	#						posts=posts)
	
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
							title='Sign In',
							form=form)