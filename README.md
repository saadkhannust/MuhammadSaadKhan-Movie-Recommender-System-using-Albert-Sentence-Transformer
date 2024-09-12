# MuhammadSaadKhan-Movie-Recommender-System-using-Albert-Sentence-Transformer

# Movie Recommender System API

This project implements a movie recommendation system using FastAPI, sentence embeddings, and cosine similarity. The application uses a pre-trained `paraphrase-albert-small-v2` model from `sentence-transformers` to encode movie data and recommend similar movies based on a given movie title.

## Features

- **FastAPI**: A high-performance API for serving recommendations.
- **Sentence Transformers**: Pre-trained BERT model `paraphrase-albert-small-v2` is used to encode movie features.
- **Cosine Similarity**: Compute similarity between movies using cosine similarity on sentence embeddings.
- **Data**: Uses a dataset with movies and tags that have been pre-processed and saved to a CSV file (`cleaned_tmdb_movies.csv`).


### Requirements & Dependencies

Python 3.8+
fastapi
uvicorn
pandas
scikit-learn
sentence-transformers
nltk
numpy 
streamlit

fast_api_app_backend_file: api.py
app_file: app2.py


###Data Cleaning
The file data-cleaning.ipynb is responible for cleaning and preprocessing of data which is the tmdb_5000_movies.csv and tmdb_5000_credit.csv so Ensure that these files are in the root directory of the project.
The output of this file is cleaned_tmdb_movies.csv which I also provided. 
Simply run the file if needed.


###Model Building and IO
This file uses Allbert pretrained transformer on the cleaned_tmdb_movies.csv and checks similarity using the cosine similarity. It also saves and loads the model.
Ensure that the cleaned_tmdb_movies.csv file is in the root directory of the project.


###api.py
This file is to run the Fast API application.
Ensure that the cleaned_tmdb_movies.csv file is in the root directory of the project.
Run the application using Uvicorn:
uvicorn api:app --reload
The API will be available at http://127.0.0.1:8000.


Endpoints:
GET /: Welcome message.
GET /recommend/{movie_name}: Get movie recommendations based on the movie_name.


Example usage:
http://127.0.0.1:8000/recommend/Batman Begins


##app2.py
Run this file along with Fast API application using "uvicorn api:app --reload" in one terminal and "streamlit run app2.py" in another.
This file gives the StreamLit application.


##Deployment on Hugging Faces
To deploy this API on Hugging Face Spaces:
Upload the project files to the Hugging Face repository.
Once uploaded, the FastAPI app will be available online.
