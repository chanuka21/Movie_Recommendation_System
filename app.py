import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = "1aa140f5fec12fb1964fc22a2d099bfa"


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.set_page_config(page_title="Movie Recommender 🎬", layout="wide")

st.markdown("<h1 style='font-size: 48px; color: #ff4b4b; text-align: center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa;'>Select a movie and get 5 similar suggestions with posters.</p>", unsafe_allow_html=True)


selected_movie_name = st.selectbox(
    '🔍 Select a movie you like:',
    movies['title'].values
)


if st.button('🎥 Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"<h4 style='text-align:center; margin-top:10px; color:#ffffff;'>{names[i]}</h4>", unsafe_allow_html=True)



st.markdown("""
    <style>
        /* Background color */
        body {
            background-color: #0e1117;
        }

        /* Center align all h4 movie titles */
        h4 {
            text-align: center;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
            font-weight: bold;
        }

        /* Button styling */
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
        }

        /* Add a shadow to images */
        img {
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        }

        /* Title style */
        h1 {
            font-family: 'Segoe UI', sans-serif;
            font-size: 48px;
            color: #ff4b4b;
        }

    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            margin-top: 20px;
            border: none;
            box-shadow: 0 4px 10px rgba(255, 75, 75, 0.4);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #ff1a1a !important;
            color: #fff !important;
            text-shadow: 0 0 5px rgba(255,255,255,0.6);
            box-shadow: 0 6px 12px rgba(255, 26, 26, 0.6);
            transform: scale(1.05);
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

