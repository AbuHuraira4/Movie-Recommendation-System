#  Movie Recommendation System

This is a **Movie Recommendation Web App** built using **Streamlit** and **Machine Learning**.  
It suggests similar movies based on your selected movie using **cosine similarity** on movie features.  
Movie posters are fetched dynamically from the **TMDB API**.

---

##  Features
- Search and select a movie from the list.
- Get **top 10 similar movies** recommended.
- Posters are displayed for each recommendation.
- Simple and interactive Streamlit UI.

---

##  Dataset
- The dataset is **not included** in this repo.  
- Download it from Kaggle  link  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata.  
- Place the dataset in the same folder where you clone this project.

---

##  How It Works
- `.pkl` files (`movie_list.pkl` and `similarity.pkl`) are **not included** here.  
- When you run the Jupyter Notebook, these files will be **generated automatically**.  
- The Streamlit app then uses these files to make recommendations.

---

## ▶ Run the App
1. Open a terminal (VS Code or any Python terminal).
2. Run the app:
   streamlit run setup.py
