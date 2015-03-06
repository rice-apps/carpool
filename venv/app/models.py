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