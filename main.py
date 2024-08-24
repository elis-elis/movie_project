from movie_app import MovieApp
from storage_json import StorageJson


def main():
    # Create a StorageJson object with the desired JSON file
    storage = StorageJson('movies.json')

    # Create a MovieApp object with the StorageJson object
    movie_app = MovieApp(storage)

    # Run the app
    movie_app.run()


# Ensure the main function is called when this file is executed
if __name__ == "__main__":
    main()
