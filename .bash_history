neofetch
uname -a
neofetch
uname
uname -a
exit
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/main.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/main.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/main.py
print(search_movie_by_title("Inception")
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/main.py print(search_movie_by_title("Inception")
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/main.py print(search_movie_by_title("Inception")
uname -a
exit
uname -a
pwd
pwd
cd /teamspace/studios/this_studio
la
ls
code .
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
lightning run app app.py
lightning run --app app.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
lightning run --app app.py
pip install lightning
pip show lightning
pip show lightning
python3 run app.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
pip install lightning[app]
pip install "lightning>=2.0.0" "lightning-app>=2.0.0"
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
clear
pip install gradio
clear
pip show lightning.app
clear
pip list | grep -i lightning
pip list | grep -i lightning
pip install "lightning[app]" lightning-app
pip list | grep -i "lightning-app\|lightning_app"
clear
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
sudo apt install neofetch
neofetchneofetch
neofetch
clear
clclear
clear
exit
cd
ls -a
pwr
pwd
code .
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
pip install --upgrade lightning
:contentReference[oaicite:20]{index=20}
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
/home/zeus/miniconda3/envs/cloudspace/bin/python /teamspace/studios/this_studio/app.py
code .
print(recommend_movies("Action", "Long", "Bay"))
print(recommend_movies("Action", "Long", "Bay"))
print(recommend_movies("Action","Long",)
python
python test_recommend.py
python test_recommend.py
python test_recommend.py
python test_recommend.py
python test_recommend.py
python test_recommend.py
python test_recommend.py
import gradio as gr
from movie_db import recommend_movies
def recommend_movies_ui(title, genre, duration, director):
    movies = recommend_movies(genre, duration, director if director else None)
    if not movies:;         return "No matching movies found."         output = "";     for movie in movies:;         title, genre, director, duration = movie[1], movie[2], movie[3], movie[4]
        output += f"🎬 {title} | 🎭 {genre} | 🎬 Dir: {director} | ⏱ {duration} mins\n"
    return output
genres = ["Sci-Fi", "Action", "Drama", "Animation", "Romance", "Adventure", "Fantasy", "Biography", "Musical", "Crime"]
duration_choices = ["Short (0-90 mins)", "Medium (90-120 mins)", "Long (120+ mins)"]
iface = gr.Interface(
    fn=recommend_movies_ui,
    inputs=[
        gr.Textbox(label="Genre"),
        gr.Radio(choices=["short", "long", "any"], label="Duration"),
        gr.Textbox(label="Director (optional)")
    ],
    outputs="text"
)
python web_interface.py]
python web_interface.py
python app.py
pip install flask
python app.py
python app.py
