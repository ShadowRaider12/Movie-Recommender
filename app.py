from flask import Flask, render_template, request, flash
from movie_db import recommend_movies

app = Flask(__name__)
app.secret_key = "n3xus_2025_movie_recs"


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        genre = request.form.get("genre", "").strip()
        duration = request.form.get("duration", "").strip()
        director = request.form.get("director", "").strip()

        if genre == "":
            flash("Please select a genre.", "warning")
        elif duration not in ["short", "medium", "long", "any"]:
            flash("Invalid duration selected.", "warning")
        else:
            recommendations = recommend_movies(
                genre,
                duration if duration else "any",
                director if director else None
            )
            if not recommendations:
                flash("No matching movies found.", "info")

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)