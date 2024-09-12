
import streamlit as st
import requests
import pandas as pd

st.title('Movie Recommender System')

# API URL (assuming FastAPI is running locally on port 8000)
api_url = "http://127.0.0.1:8000/recommend/"

# Load the list of movie names
new_df = pd.read_csv('cleaned_tmdb_movies.csv')
movie_list = new_df['title'].values

# Streamlit dropdown to select a movie
movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# When the button is clicked, make a request to the FastAPI backend
if st.button('Show Recommendation'):
    try:
        response = requests.get(api_url + movie_name)
        recommendations = response.json().get('recommendations', [])

        if recommendations:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommendations[0])
            with col2:
                st.text(recommendations[1])
            with col3:
                st.text(recommendations[2])
            with col4:
                st.text(recommendations[3])
            with col5:
                st.text(recommendations[4])
        else:
            st.error("No recommendations found.")
    except Exception as e:
        st.error(f"Error: {e}")
