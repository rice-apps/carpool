from flask import render_template, redirect, session, request
from flask import make_response, jsonify
from app import app, db
from app.trips import delete_old
from .models import Trip


@app.route('/newtrip', methods=['GET', 'POST'])
def newtrip():
    # Validation now just ensures no fields are empty, should check that times are valid
    if request.method == "POST":
        form = request.json
        print request
        print form
        t = Trip(origin=form['origin'],
                 destination=form['destination'],
                 contact_info=form['contact'],
                 date=form['date'][:10],
                 TOA=form['arrival_time'],
                 TOD=form['depart_time'],
                 seats=form['seats_num'])
        db.session.add(t)
        db.session.commit()
        return redirect('/index')  # if successful post, return to home page

    return render_template('newtrip.html',
                           title='Post a new trip')


@app.route('/')
@app.route('/index')
def index():
    # User Net ID
    login = session.get(app.config['CAS_USERNAME_SESSION_KEY'], None)

    # Check if there someone logged in
    if login is None:
        return make_response(open('app/static/templates/login.html').read())
    else:
        return make_response(open('app/static/templates/index.html').read())


@app.route('/trips')
def get_trips():
    trips = Trip.query.all()
    delete_old(trips)
    trips_list = map(Trip.to_json, trips)
    result = {"trips": trips_list}

    return jsonify(result)
