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
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=2)


def add_movie(file_path, title, year, rating, poster_url):
    """
    Add a movie to the database. The movie details include title, year,
    rating, and poster URL.
    """
    movies = load_movies(file_path)

    if title in movies:
        print(f"Oh hunny, the movie {title} is already there, pick another movie.")
        # Update only if necessary
        if not movies[title].get('year'):
            movies[title]['year'] = year
        if not movies[title].get('rating'):
            movies[title]['rating'] = rating
        if not movies[title].get('poster_url'):
            movies[title]['poster_url'] = poster_url
    else:
        # Add new movie
        movies[title] = {
            'year': year,
            'rating': rating,
            'poster_url': poster_url
        }

    save_movies(file_path, movies)


def delete_movie(file_path, title_input):
    """
    Deletes a movie from the movies' database.
    Loads the information from the JSON file, deletes the movie,
    and saves it.
    """
    movies = load_movies(file_path)
    # Find the actual title in a case-insensitive manner
    title_to_delete = None
    for title in movies.keys():
        if title.lower() == title_input.lower():
            title_to_delete = title
            break

    if title_to_delete:
        del movies[title_to_delete]
        save_movies(file_path, movies)
        return True
    else:
        return False


def update_movie(file_path, title, note):
    """
   Updates a movie from the movies database with a note.
   Loads the information from the JSON file, updates the movie,
   and saves it.
   """
    movies = load_movies(file_path)
    # Convert title to lowercase for case-insensitive matching
    title_lower = title.lower()

    for movie_title in list(movies.keys()):
        if movie_title.lower() == title_lower:
            # Found the movie to update
            movies[movie_title]['note'] = note
            save_movies(file_path, movies)
            return True

    return False
