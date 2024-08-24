import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_movies(self):
        """
        Load the movies from the JSON file.
        """
        try:
            with open(self.file_path, 'r') as file:
                movies = json.load(file)
                if not isinstance(movies, dict):
                    movies = {}
        except (FileNotFoundError, json.JSONDecodeError):
            movies = {}
        return movies

    def save_movies(self, movies):
        """
        Save the movies to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=2)

    def add_movie(self, title, year, rating, poster_url):
        """
        Add a movie to the JSON file.
        """
        movies = self.load_movies()
        if title in movies:
            raise ValueError(f"Movie '{title}' already exists.")
        movies[title] = {'year': year, 'rating': rating, 'poster_url': poster_url}
        self.save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the JSON file.
        """
        movies = self.load_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)
        else:
            raise ValueError(f"Movie '{title}' not found.")

    def update_movie(self, title, note):
        """
        Update a movie with a note.
        """
        movies = self.load_movies()
        if title in movies:
            movies[title]['note'] = note
            self.save_movies(movies)
        else:
            raise ValueError(f"Movie '{title}' not found.")
