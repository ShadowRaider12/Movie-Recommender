from flask import Flask, render_template, request
from movie_db import recommend_movies

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        genre = request.form.get('genre')
        duration_pref = request.form.get('duration')
        director = request.form.get('director')

        recommendations = recommend_movies(genre, duration, director if director else None)   
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)