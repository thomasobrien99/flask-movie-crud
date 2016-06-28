from flask import Flask, url_for, request, redirect, render_template
from flask_modus import Modus

from models.shared import db
from models.tag import Tag
from models.director import Director
from models.movie import Movie

app = Flask(__name__)
modus = Modus(app)

'''WHAT IS ALL THIS DOING?'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_movie_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.url_map.strict_slashes = False
db.init_app(app)
with app.app_context():
    db.create_all()
''' '''

@app.route('/')
def index():
	return render_template('index.html')


# Director Routes
@app.route('/directors', methods=['GET'])
def index_director():
	dirs = Director.query.all()
	return render_template('directors/index.html', dirs=dirs)

@app.route('/directors', methods=['POST'])
def add_director():
	new_dir = Director(request.form['name'])
	db.session.add(new_dir)
	db.session.commit()
	return redirect(url_for('index_director'))

@app.route('/directors/new')
def new_director():
	return render_template('directors/new.html')

@app.route('/directors/<int:id>')
def show_director(id):
	show_dir = Director.query.get(id)
	return render_template('/directors/show.html', dir=show_dir)

@app.route('/directors/<int:id>/edit')
def edit_director(id):
	edit_dir = Director.query.get(id)
	return render_template('/directors/edit.html', dir=edit_dir)

@app.route('/directors/<int:id>', methods=['PATCH'])
def update_director(id):
	update_dir = Director.query.get(id)
	update_dir.name = request.form['name']
	db.session.add(update_dir)
	db.session.commit()
	return redirect(url_for('index_director'))

@app.route('/directors/<int:id>', methods=['DELETE'])
def destroy_director(id):
	delete_dir = Director.query.get(id)
	db.session.delete(delete_dir)
	db.session.commit()
	return redirect(url_for('index_director'))

# Movie Routes
@app.route('/directors/<int:id>/movies')
def index_movie(id):
	director = Director.query.get(id)
	return render_template('movies/index.html', director=director)

@app.route('/directors/<int:id>/movies', methods=["POST"])
def add_movie(id):
	new_movie = Movie(request.form['title'], id)
	db.session.add(new_movie)
	db.session.commit()
	return redirect(url_for('index_movie', id=id))

@app.route('/directors/<int:id>/movies/new')
def new_movie(id):
	director = Director.query.get(id)
	return render_template('movies/new.html', director=director)

@app.route('/directors/<int:id>/movies/<int:movie_id>/edit')
def edit_movie(id,movie_id):
	movie = Movie.query.get(movie_id)
	return render_template('movies/edit.html', movie=movie)

@app.route('/directors/<int:id>/movies/<int:movie_id>', methods=["GET"])
def show_movie(id,movie_id):
	movie = Movie.query.get(movie_id) # IS THIS BUILT IN EXPECTING "ID"?
	return render_template('movies/show.html', movie=movie)

@app.route('/directors/<int:id>/movies/<int:movie_id>', methods=["PATCH"])
def update_movie(id,movie_id):
	movie = Movie.query.get(movie_id)
	movie.title = request.form["title"]
	db.session.add(movie)
	db.session.commit()
	return redirect(url_for('index_movie', id=id))

@app.route('/directors/<int:id>/movies/<int:movie_id>', methods=["DELETE"])
def destroy_movie(id,movie_id):
	movie = Movie.query.get(movie_id) # what does get_or_404 do?
	db.session.delete(movie)
	db.session.commit()
	return redirect(url_for('index_movie', id=id))

#tag routes
@app.route('/tags')
def index_tag():
	tags = Tag.query.all()
	return render_template('tags/index.html', tags=tags)

@app.route('/tags', methods=['POST'])
def create_tag():
  tag = Tag(request.form["name"])
  db.session.add(tag)
  db.session.commit()
  return redirect(url_for('index_tag'))

@app.route('/tags/new')
def new_tag():
	return render_template('tags/new.html')

@app.route('/tags/<int:id>')
def show_tag(id):
	tag = Tag.query.get(id)
	return render_template('tags/show.html', tag=tag)

@app.route('/tags/<int:id>/edit')
def edit_tag(id):
	tag = Tag.query.get(id)
	return render_template('tags/edit.html', tag=tag)

@app.route('/tags/<int:id>', methods=['PATCH'])
def update_tag(id):
  tag = Tag.query.get(id)
  tag.name = request.form['name'];
  db.session.add(tag)
  db.session.commit()
  return redirect(url_for('index_tag'))

@app.route('/tags/<int:id>', methods=['DELETE'])
def destroy_tag(id): 
	tag = Tag.query.get(id)
	db.session.delete(tag)
	db.session.commit()
	return redirect(url_for('index_tag'))


if __name__ == '__main__':
	app.run(debug=True, port=3000);