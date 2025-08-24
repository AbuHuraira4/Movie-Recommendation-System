import pickle
import streamlit as st
import requests

st.header("🎬 Movie Recommendation System")

# Load data
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values
selected_movie = st.selectbox("Enter a movie to get recommendation", movie_list)

# Function to fetch poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=529e07e22fbf92fa6bcf922b307a9c08&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommend_movie_names = []
    recommend_movie_posters = []
    
    for i in distances[1:6]:  # top 5
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie_names.append(movies.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    
    return recommend_movie_names, recommend_movie_posters

# Display in Streamlit
if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
