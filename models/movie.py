from models.shared import db
# WHY IS THIS HERE AND NOT SOMEWHERE ELSE?
movie_tags = db.Table('movie_tags',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
	db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))
)

class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text())
	director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
	tags = db.relationship('Tag', secondary='movie_tags', backref=db.backref('movies', lazy='dynamic'))
  #GOT WEIRD ERROR WHEN 'Tag' was 'tag'
	#WHAT DOES SECONDARY DO? WHAT DOES LAZY DO?
	def __init__ (self, title, director_id):
		self.title = title
		self.director_id = director_id