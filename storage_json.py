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
            with open(self.file_path, 'r', encoding="utf-8") as file:
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
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(movies, file, indent=2)
