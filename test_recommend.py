from movie_db import recommend_movies

# Change these values to test different searches
genre = "Action"
duration = "Long"
director = "Ridley Scott"

results = recommend_movies(genre, duration, director)

# Print results nicely
if results:
    for movie in results:
        print(f"Title: {movie[1]} | Genre: {movie[2]} | Director: {movie[3]} | Duration: {movie[4]} mins")
else:
    print("No matching movies found.")
