import pandas as pd

def load_movielens(path='data/movies.csv'):
    df = pd.read_csv(path)
    df['genres'] = df['genres'].str.replace('|', ' ', regex=False)
    return df