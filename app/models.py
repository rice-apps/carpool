from app import db

"""
This file contains the different database models that our server
will hold.  Now, there're only two sample ones, called User and Post.
User holds an integer called ID, two strings (a nickname
and an email), and the posts related to that User.  
Post contains an ID, body, timestamp, and a field called 
user_id which essentially points to a User

See:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
for more on the relationship between User and Post, and how to access one from the other
"""


class User(db.Model):
	# Structure of the data held in a User
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	# For printing
	def __repr__(self):
		return '<User %r>' % (self.nickname)
		
class Post(db.Model):
	# Structure of the data held in a Post
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	# For printing
	def __repr__(self):
		return '<Post %r>' % (self.body)

class Trip(db.Model):
    # Structure of the data held in a Trip
    id = db.Column(db.Integer, primary_key=True)
    net_id = db.Column(db.Integer, index=True)
    origin = db.Column(db.String(64), index=True, unique=True) #Thought: break up into subsections (street, city, etc) for standardization
    destination = db.Column(db.String(64), index=True, unique=True) #Thought: break up into subsections (street, city, etc) for standardization
    contact_info = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.String(8), index=True, unique=True)
    TOD = db.Column(db.String(8), index=True, unique=True)#Time Of Departure, form: "HH:MM"
    TOA = db.Column(db.String(8), index=True, unique=True)#Time Of Arrival, form: "HH:MM"
    seats = db.Column(db.String(8), index=True, unique=True)
    # For printing

    def __repr__(self):
        return '<Post %r>' % (self.body)

    def to_json(self):
        return {
        "net_id" : self.net_id,
        "origin" : self.origin,
        "destination" : self.destination,
        "contact_info" : self.contact_info,
        "date" :  self.date,
        "TOD" : self.TOD,
        "TOA" : self.TOA,
        "seats" : self.seats
        }
