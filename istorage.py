from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def load_movies(self):
        """
        Load the movies from the storage.
        """
        pass

    @abstractmethod
    def save_movies(self, movies):
        """
        Save the movies to the storage.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url):
        """
        Add a movie to the storage.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage.
        """
        pass

    @abstractmethod
    def update_movie(self, title, note):
        """
        Update a movie with a note.
        """
        pass
