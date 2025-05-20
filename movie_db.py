import sqlite3

def recommend_movies(genre, duration_pref, director = None):
    conn = sqlite3.connect("movie_app.sqlite3")
    cursor = conn.cursor()
    
    if duration_pref == "Short":
        duration_condition = "duration < 90"
    if duration_pref == "Medium":
        duration_condition == "duration BETWEEN 90 AND 120"
    if duration_pref == "Long":
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
        cursor.execute(F"""
            SELECT * FROM movies
            WHERE genre = ?
            AND {duration_condition}
            """, (genre,))
    
    results = cursor.fetchall()
    conn.close
    return results