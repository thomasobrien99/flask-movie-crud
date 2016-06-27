from flask import Flask, url_for, request, redirect, render_template
from flask_modus import Modus

from models.movie import Movie


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, port=3000);