import json


def load_movies():
    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)
            if not isinstance(movies, dict):
                movies = {}
    except FileNotFoundError:
        movies = {}
    return movies


def save_movies(movies):
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=2)


def add_movie(title, year, rating, poster_url):
    movies = load_movies()
    movies[title] = {'year': year, 'rating': rating, 'poster_url': poster_url}
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = load_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)


# def update_movie(title, rating):
   # """
   # Updates a movie from the movies database.
   # Loads the information from the JSON file, updates the movie,
   # and saves it. The function doesn't need to validate the input.
   # """
   # movies = load_movies()
   # if title in movies:
   #     movies[title]['rating'] = rating
   #     save_movies(movies)
