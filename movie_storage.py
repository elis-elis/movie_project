import json


def load_movies(file_path):
    """
    Load the movies from the JSON file. If the file is not found,
    or if the content is not a dictionary, return an empty dictionary.
    """
    try:
        with open(file_path, "r") as file:
            movies = json.load(file)
            if not isinstance(movies, dict):
                movies = {}
    except (FileNotFoundError, json.JSONDecodeError):
        # to ensure the function handles errors when the JSON file is corrupted.
        movies = {}
    return movies


def save_movies(file_path, movies):
    """
    Save the movies to the JSON file with pretty indentation.
    """
    with open(file_path, "w") as file:
        json.dump(movies, file, indent=2)


def add_movie(title, year, rating, poster_url):
    """
    Add a movie to the database. The movie details include title, year,
    rating, and poster URL.
    """
    movies = load_movies()
    movies[title] = {'year': year, 'rating': rating, 'poster_url': poster_url}
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it.
    """
    movies = load_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)


def update_movie(file_path, title, note):
    """
   Updates a movie from the movies database with a note.
   Loads the information from the JSON file, updates the movie,
   and saves it.
   """
    movies = load_movies(file_path)
    if title in movies:
        movies[title]['note'] = note
        save_movies(file_path, movies)
        return True
    return False
