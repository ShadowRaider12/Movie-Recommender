import gradio as gr
from movie_db import recommend_movies

def recommend_movies_ui(genre, duration, director):
    movies = recommend_movies(genre, duration, director if director else None)
    if not movies:
        return "No matching movies found."
    
    output = ""
    for movie in movies:
        title, genre, director, duration = movie[1], movie[2], movie[3], movie[4]
        output += f"🎬 {title} | 🎭 {genre} | 🎬 Dir: {director} | ⏱ {duration} mins\n"
    return output

genres = ["Sci-Fi", "Action", "Drama", "Animation", "Romance", "Adventure", "Fantasy", "Biography", "Musical", "Crime"]
duration_choices = ["Short (0-90 mins)", "Medium (90-120 mins)", "Long (120+ mins)"]

iface = gr.Interface(
    fn=recommend_movies_ui,
    inputs=[
        gr.Dropdown(choices = genres, label="Genre", interactive=True),
        gr.Radio(duration_choices, label="Duration Preference"),
        gr.Textbox(label="Director (optional)")
    ],
    outputs="text"
)

iface.launch()