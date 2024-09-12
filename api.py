# api.py
from fastapi import FastAPI, HTTPException
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn

app = FastAPI()

# Load data
new_df = pd.read_csv('cleaned_tmdb_movies.csv')


# Function to combine features
def combine_features(row):
    return row['title'] + ' ' + row['tags']


new_df['combined_value'] = new_df.apply(combine_features, axis=1)
new_df['index'] = [i for i in range(0, len(new_df))]

# Load pre-trained BERT model for encoding
bert = SentenceTransformer('paraphrase-albert-small-v2')
sentence_embeddings = bert.encode(new_df['combined_value'].tolist())

# Compute similarity
similarity = cosine_similarity(sentence_embeddings)


# Helper functions to get movie title and index
def get_title(index):
    return new_df[new_df.index == index]["title"].values[0]


def get_index(title):
    try:
        return new_df[new_df.title == title]["index"].values[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="Movie not found")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommender System API"}


@app.get("/recommend/{movie_name}")
def recommend_movie(movie_name: str):
    try:
        movie_idx = get_index(movie_name)
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=e.detail)

    movie_recommendation = sorted(
        list(enumerate(similarity[movie_idx])),
        key=lambda x: x[1], reverse=True
    )[1:6]  # Top 5 recommendations excluding the input movie

    recommended_movies = [get_title(rec[0]) for rec in movie_recommendation]

    return {"recommendations": recommended_movies}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

