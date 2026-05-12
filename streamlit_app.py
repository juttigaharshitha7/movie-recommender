import streamlit as st
import pandas as pd
from src.data_loader import load_movielens
from src.recommender import ContentBasedRecommender

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommendation System")
st.markdown("Find movies similar to your favorites!")

@st.cache_resource
def load_recommender():
    movies = load_movielens('data/movies.csv')
    recommender = ContentBasedRecommender(movies)
    return recommender, movies

with st.spinner("Loading movies..."):
    recommender, movies = load_recommender()

st.success(f"✅ {len(movies)} movies loaded!")

movie_input = st.text_input("🔍 Enter a movie title:", placeholder="e.g. Toy Story, Jumanji, Heat")

num_recommendations = st.slider("Number of recommendations:", 3, 10, 5)

if st.button("🎯 Get Recommendations"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie title!")
    else:
        results = recommender.recommend(movie_input, top_n=num_recommendations)
        if isinstance(results, list):
            st.markdown(f"### ✅ You might also like:")
            for i, movie in enumerate(results, 1):
                st.markdown(f"**{i}.** 🎥 {movie}")
        else:
            st.error(results)

st.markdown("---")
st.markdown("Built with ❤️ using Python & Streamlit | Data: MovieLens")