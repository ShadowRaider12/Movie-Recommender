import sqlite3

def recommend_movies(genre, duration_pref, director = None):
    conn = sqlite3.connect("movie_app.sqlite3")
    cursor = conn.cursor()
    
    duration_pref = duration_pref.lower()

    if duration_pref == "short":
        duration_condition = "duration < 90"
    elif duration_pref == "medium":
        duration_condition = "duration BETWEEN 90 AND 120"
    elif duration_pref == "long":
        duration_condition = "duration > 120"
    else:
        duration_condition = "1=1"
    
    if director:
        cursor.execute(f"""
            SELECT * FROM movies
            WHERE genre = ?
            AND {duration_condition}
            AND director LIKE ?
        """, (genre, f"%{director}%"))
    else:
        cursor.execute(f"""
            SELECT * FROM movies
            WHERE genre = ?
            AND {duration_condition}
            """, (genre,))
    
    results = cursor.fetchall()
    conn.close()
    return results