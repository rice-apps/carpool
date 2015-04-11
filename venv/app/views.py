#not all of these imports used
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import send_from_directory, make_response, jsonify
from app import app, db#,oid, lm
from .forms import LoginForm, NewTripForm
from .models import User
from .models import Trip


@app.route('/newtrip', methods=['GET','POST'])
def newtrip():
    form = NewTripForm()
    # Validation now just ensures no fields are empty, should check that times are valid
    if request.method == "POST":
        form = request.json
        print request
        print form
        #if form.validate(request.json):
        #flash("Received trip from %s to %s" % (form.destination.data, form.origin.data))
        t = Trip(origin=form['origin'],
                 destination=form['destination'],
                 contact_info=form['contact'],
                 date=form['date'],
                 TOA=form['arrival_time'],
                 TOD=form['depart_time'])
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


    return make_response(open('app/static/templates/index.html').read())
    #return send_from_directory('static/templates', 'index.html')



    #user = {'nickname': 'Miguel'} #fake user
    #db_user = User.query.filter_by(nickname=user['nickname']).first()
    #posts = db_user.posts.all()


@app.route('/trips')
def get_trips():
    trips = Trip.query.all()
    trips_list = map(Trip.to_json, trips)
    print trips_list
    result = { "trips": trips_list }

    return jsonify(result)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)