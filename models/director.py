from models.shared import db

class Director(db.Model):
	__tablename__  = 'directors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text())
	movies = db.relationship('Movie', backref='director', lazy='dynamic') # WHAT IS THIS DOING?

	def __init__ (self, name):
		self.name = name