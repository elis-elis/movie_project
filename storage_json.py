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
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(movies, file, indent=2)

    def add_movie(self, title, year, rating, poster_url):
        """
        Add a movie to the JSON file.
        """
        movies = self.load_movies()
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

        self.save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the JSON file.
        """
        movies = self.load_movies()
        title_to_delete = None

        # Convert the input title to lowercase once for comparison
        title_lower = title.lower()

        # Find the actual title in a case-insensitive manner
        for stored_title in movies.keys():
            if stored_title.lower() == title.lower():
                title_to_delete = stored_title
                break

        if title_to_delete:
            del movies[title_to_delete]
            self.save_movies(movies)
            return True

        return False

    def update_movie(self, title, note):
        """
        Update a movie with a note.
        """
        movies = self.load_movies()
        # Convert title to lowercase for case-insensitive matching
        title_lower = title.lower()

        for movie_title in list(movies.keys()):
            if movie_title.lower() == title_lower:
                # Found the movie to update
                movies[movie_title]['note'] = note
                self.save_movies(movies)
                return True

        return False
