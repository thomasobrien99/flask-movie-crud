from flask import Flask, url_for, request, redirect, render_template
from flask_modus import Modus

from models.shared import db
from models.movie import Movie


app = Flask(__name__)

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

# Movie Routes
@app.route('/movies')
def index_movie():
	movies = Movie.query.all();
	return render_template('movies/index.html', movies=movies)

@app.route('/movies', methods=["POST"])
def add_movie():
	new_movie = Movie(request.form['title'])
	db.session.add(new_movie)
	db.session.commit()
	return redirect(url_for('index_movie'))

@app.route('/movies/new')
def new_movie():
	return render_template('movies/new.html')

if __name__ == '__main__':
	app.run(debug=True, port=3000);