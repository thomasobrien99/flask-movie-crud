from models.shared import db

class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text())
	# director_id = db.Column(db.Integer)
	def __init__ (self, title):
		self.title = title