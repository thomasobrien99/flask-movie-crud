from models.shared import db

class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text()) #WHY IS THIS A METHOD IF INTEGER IS NOT
	
	def __init__(self, name):
		self.name = name