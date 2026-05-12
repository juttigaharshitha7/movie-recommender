from src.data_loader import load_movielens
from src.recommender import ContentBasedRecommender

def main():
    print("🎬 Movie Recommendation System")
    movies = load_movielens('data/movies.csv')
    recommender = ContentBasedRecommender(movies)

    while True:
        movie = input("\nEnter a movie title (or 'quit'): ")
        if movie.lower() == 'quit':
            break
        results = recommender.recommend(movie)
        if isinstance(results, list):
            print("\n✅ You might also like:")
            for i, r in enumerate(results, 1):
                print(f"  {i}. {r}")
        else:
            print(results)

if __name__ == "__main__":
    main()