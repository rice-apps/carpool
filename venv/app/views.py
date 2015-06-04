#not all of these imports used
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import send_from_directory, make_response, jsonify
from app import app, db#,oid, lm
from .forms import LoginForm, NewTripForm
from .models import User
from .models import Trip
from sqlalchemy import delete
from datetime import date

app.config['CAS_SERVER'] = 'https://netid.rice.edu'
app.config['CAS_AFTER_LOGIN'] = 'index'
app.config['APP_URL'] = "http://localhost:5000"

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
                 date=form['date'][:10],
                 TOA=form['arrival_time'],
                 TOD=form['depart_time'],
				 seats=form['seats_num'])

        db.session.add(t)
        db.session.commit()
        return redirect('/index') # if successful post, return to home page

    return render_template('newtrip.html',
                       title='Post a new trip',
                       form=form)

@app.route('/')
@app.route('/index')
def index():

    # User Net ID
    login = session.get(app.config['CAS_USERNAME_SESSION_KEY'], None)

    # Check if there someone logged in
    if login is None:
        # Send login page
        return make_response(open('app/static/templates/login.html').read())
    else:
        # Send home page
        return make_response(open('app/static/templates/index.html').read())


def delete_old(trips):
    today = str(date.today())

    print "\nToday's date: " + today

    for trip in trips:
        this_date = trip.date
        print "Trip w/ date: " + this_date
        if this_date < today:
            print this_date + " is before today, need to delete"
            db.session.delete(trip)
            db.session.commit()
            trips.remove(trip)


@app.route('/trips')
def get_trips():
    trips = Trip.query.all()
    delete_old(trips)
    trips_list = map(Trip.to_json, trips)
    print trips_list
    result = { "trips": trips_list }

    return jsonify(result)