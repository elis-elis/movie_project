import csv

from istorage import IStorage
from typing import Dict, Any


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path

    def load_movies(self) -> Dict[str, Dict[str, Any]]:
        """
        Load movies from a CSV file and return a dictionary.
        """
        # Each row in the CSV file corresponds to an entry in the dictionary.
        # The movie title serves as the key, and the associated details
        # (year, rating, poster URL, and optional notes) are stored as values in a nested dictionary.
        movies = {}
        try:
            with open(self._file_path, mode='r', newline='', encoding='utf-8') as file:
                # Reads the CSV file and parses each row into a dictionary
                # where the keys are the column headers from the first row of the CSV file.
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        'year': row['year'],
                        'rating': row['rating'],
                        'poster_url': row['poster_url'],
                        'notes': row.get('notes', '')
                    }
        except FileNotFoundError:
            # If file doesn't exist, return an empty dictionary
            pass
        return movies

    def save_movies(self, movies: Dict[str, Dict[str, str]]) -> None:
        """
        Save movies to CSV file from a dictionary.
        This function uses the csv module to write data into a CSV file in a structured format.
        """
        with open(self._file_path, mode='w', newline='', encoding='utf-8') as file:
            # Specifies the order of columns in the CSV file.
            # This list should match the keys used in the dictionary.
            fieldnames = ['title', 'year', 'rating', 'poster_url', 'notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Writes the header row to the CSV file using the column names specified in 'fieldnames'.
            writer.writeheader()

            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'year': details['year'],
                    'rating': details['rating'],
                    'poster_url': details['poster_url'],
                    'notes': details.get('notes', '')
                })

    def add_movie(self, title, year, rating, poster_url):
        """
        Add a new movie to the CSV file.
        """
        movies = self.load_movies()
        movies[title] = {
            'year': year,
            'rating': rating,
            'poster_url': poster_url,
            'notes': ''
        }
        self.save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the CSV file.
        If the movie is successfully deleted, the function returns True.
        If no matching movie is found, it returns False.
        """
        movies = self.load_movies()

        # This variable will later hold title of the movie that needs to be deleted, if found.
        title_to_delete = None
        for movie_title in movies:
            if movie_title.lower() == title.lower():
                title_to_delete = movie_title
                break
                # no need to continue looping since the movie to delete has been identified.

        if title_to_delete:
            # if it's not None, means that a movie with the specified title was found.
            del movies[title_to_delete]
            self.save_movies(movies)
            return True

        return False

    def update_movie(self, title, note):
        """
        Update the note of the movie in the CSV file.
        The function returns True if a movie was found and updated,
        and False if no movie with the provided title was found.
        """
        movies = self.load_movies()
        title_lower = title.lower()

        for movie_title in list(movies.keys()):
            # movies.keys() returns a view of all the keys (movie titles) in the dictionary,
            # and list() converts that view into a list, so we can iterate over it.
            if movie_title.lower() == title_lower:
                # the code compares its lowercase version (movie_title.lower())
                # with the lowercase version of the user-provided title (title_lower).
                movies[movie_title]['notes'] = note
                self.save_movies(movies)
                return True

        return False
        # indicates that no movie with the provided title was found in the CSV file,
        # so no update was made.
