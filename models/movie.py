from models.shared import db

class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text())
	director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))

	def __init__ (self, title, director_id):
		self.title = title
		self.director_id = director_id