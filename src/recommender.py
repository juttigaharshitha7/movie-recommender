import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, movies_df):
        self.movies = movies_df
        self.similarity_matrix = None
        self._build_model()

    def _build_model(self):
        self.movies['features'] = self.movies['genres'].fillna('') + ' ' + self.movies['title']
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies['features'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend(self, movie_title, top_n=5):
        mask = self.movies['title'].str.lower().str.contains(movie_title.lower(), na=False)
        matches = self.movies[mask]
        if matches.empty:
            return f"Movie '{movie_title}' not found."
        idx = matches.index[0]
        print(f"Matched: {self.movies['title'].iloc[idx]}")
        scores = list(enumerate(self.similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        return self.movies['title'].iloc[[i[0] for i in scores]].tolist()