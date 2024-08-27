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
        # (year, rating, poster URL, optional notes) are stored as values in a nested dictionary.
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
