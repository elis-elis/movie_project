import os
import requests
from dotenv import load_dotenv
from random import choice
import movie_storage
import movies_web_generator

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(movie_name):
    """
    This function sends a request to the OMDb API based on the provided movie name
    and retrieves the movie's title, year, rating, and poster URL.
    It handles
    various potential errors that may occur during the API request, including
    HTTP errors, connection errors, timeouts, and other request exceptions.

    Args:
        movie_name (str): The name of the movie to search for in the OMDb database.

    Returns:
        tuple: A tuple containing the movie's title, year, rating, and poster URL.
               If the movie is not found or an error occurs, None is returned.
    """
    try:
        api_url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}'
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError if the response status is 4xx, 5xx
        if response.status_code == requests.codes.ok:
            data = response.json()
            if data and data['Response'] == 'True':
                title = data.get('Title', 'N/A')
                year = data.get('Year', 'N/A')
                ratings = data.get('Ratings', [])
                if ratings:
                    rating = ratings[0].get('Value', 'N/A')
                else:
                    rating = 'N/A'
                poster = data.get('Poster', 'N/A')
                return title, year, rating, poster
            else:
                print("No data found for the movie:", movie_name)
                return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error happened: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error happened: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error happened: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An error happened: {req_err}")
        return None


def display_menu():
    """
    Display the main menu with options for the user.
    """
    print()
    print("°°°°°°°°°° Salut, here's E's movies app °°°°°°°°°°")
    print()
    print("Check out the Menu:")
    print()
    print("0. If you wish to exit - this is the way to go")
    print("1. (Very straightforward) it's a List of movies")
    print("2. You can Add movie(s) here")
    print("3. Say goodbye to a movie or Delete it")
    print("4. (NO more!) Update movie(s), if you have to")
    print("5. Yeap, Stats (just FYI)")
    print("6. Random movie --> for a spontaneous evening")
    print("7. Search movie, like a detective ;)")
    print("8. Movies sorted by rating (again very straightforward stuff)")
    print("9. Ahh the fun part - Generate website")
    print()


def list_movies():
    """
    This function retrieves the movie data by calling the `load_movies` function
    from the `movie_storage` module, counts the total number
    of movies, and prints each movie's title, year of release, and rating.
    """
    movies = movie_storage.load_movies()
    total_movies = len(movies)
    print(f"{total_movies} movies in total here.")
    for movie, details in movies.items():
        print(f"{movie}, year of release is {details['year']}, "
              f"and rating is {details['rating']}")


def add_movie():
    """
    Adds a movie to the movies database
    """
    try:
        title = input("Guess what. You can enter a movie name here: ")
        movie_name = fetch_data(title)

        if movie_name:
            movie_title, year, rating, poster_url = movie_name
            movie_storage.add_movie(movie_title, year, rating, poster_url)
            print("Movie Data:", movie_name)
        else:
            print("Failed to fetch data for the movie:", movie_name)

    except ValueError as error:
        print("Oh nooo! That will not work here. "
              "Please enter a valid name for the search to happen.", error)


def delete_movie():
    """
    Delete a movie from the database.
    """
    title = input("You can enter a name of the movie you would like to delete here: ")
    movies = movie_storage.load_movies()
    movie_storage.delete_movie(title)
    if title not in movies:
        print("Hello to the error! There's no such movie. Shall we try again?")
    else:
        del movies[title]
        print("As you wished - This movie has been deleted successfully.")


"""
def update_movie():
    movies = movie_storage.load_movies()
    title = input("Why don't you Enter the movie you want to find here: ")
    if title in movies:
        rating = float(input("What is the new rating for this movie? "))
        movies[title] = rating
        movie_storage.update_movie(title, rating)
        print("Voila! your rating has been updated successfully.")
    else:
        print("Oh. It's an error!")
"""


def movie_statistics():
    """
    Display statistics about the movies in the database,
    including average rating, median rating,
    best movie by rating, and worst movie by rating.
    """
    movies = movie_storage.load_movies()

    if not movies:
        print("No movies available to show statistics.")
        return

    # Average rating
    ratings = []
    for details in movies.values():
        ratings.append(float(details['rating'].split('/')[0]))
    average_movie_rating = sum(ratings) / len(ratings)
    print(f"Average rating: {average_movie_rating:.2f}")

    # Median rating
    sorted_ratings = sorted(ratings)
    length = len(sorted_ratings)
    if length % 2 == 0:
        median_movie_rating = (sorted_ratings[length // 2] + sorted_ratings[length // 2 - 1]) / 2
    else:
        median_movie_rating = sorted_ratings[length // 2]
    print("Median rating:", median_movie_rating)

    # best movie:
    max_rating = max(ratings)
    # movies.items() returns key-value pairs.
    # Each pair is a tuple with: movie title and dictionary containing the movie's details.
    best_movies = [title for title, details in movies.items()
                   if float(details['rating'].split('/')[0].replace(',', '.')) == max_rating]
    # combines all the movie titles into a single string, with each title separated by a comma and a space.
    print(f"Best movie(s): {', '.join(best_movies)}, Rating {max_rating}")

    # The worst movie by rating
    min_rating = min(ratings)
    worst_movies = [title for title, details in movies.items()
                    if float(details['rating'].split('/')[0].replace(',', '.')) == min_rating]
    print(f"Worst movie(s): {', '.join(worst_movies)}, Rating {min_rating}")


def random_movie():
    """
    Select a random movie from the database and display its title, year of release and rating.
    """
    movies = movie_storage.load_movies()
    movie, details = choice(list(movies.items()))
    print(f"Here's your movie for today: {movie}, its year of release is {details['year']}, "
          f"and it's rated: {details['rating']}.")


def search_movies_by_name():
    """
    Search for movies by name in the database and display the results.
    """
    movies = movie_storage.load_movies()
    query = input("Enter part of a movie name: ").lower()
    # Convert the query to lowercase for case-insensitive search
    matching_movies = [
        (title, details) for title, details in movies.items()
        if query in title.lower()  # Check if the query is a substring of the movie title
    ]

    if matching_movies:
        # Print each matching movie
        for title, details in matching_movies:
            print(f"{title}, its year of release: {details['year']}, "
                  f"and it's rated: {details['rating']}.")
    else:
        print(f"oops, nothing to show you from '{query}', keep searching.")


def movies_sorted_by_rating():
    """
    Sort and display the movies in the database by rating in descending order.
    """
    movies = movie_storage.load_movies()
    sorted_movies = sorted(movies.items(), key=lambda r: r[1]['rating'], reverse=True)
    for movie, details in sorted_movies:
        print(f"{movie}, its year of release: {details['year']}, "
              f"and it's rated: {details['rating']}.")


def generate_website():
    """
    Generates an HTML website from the movies database.
    """
    movies = movie_storage.load_movies()
    html_template = movies_web_generator.read_template()
    movies_html = movies_web_generator.generate_movies_info(movies)
    final_html = (html_template.replace('__TEMPLATE_TITLE__', 'E\'s Movies App').replace
                  ('__TEMPLATE_MOVIE_GRID__', movies_html))
    movies_web_generator.write_to_html_file(final_html)
    print("Voila! Your Website was generated successfully.")


def main():
    """
    Main function to run the movie database application.
    """
    # this line starts an infinite loop. It will continue running until it is terminated
    while True:
        # call function to print the menu options
        display_menu()
        enter_choice = input("and now you may Enter your choice (0-9): ")
        if enter_choice == "1":
            list_movies()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "2":
            add_movie()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "3":
            delete_movie()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "4":
            update_movie()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "5":
            movie_statistics()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "6":
            random_movie()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "7":
            search_movies_by_name()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "8":
            movies_sorted_by_rating()
            print()
            input("Press enter to continue...carefully.")
            continue
        elif enter_choice == "9":
            generate_website()
            print("Press enter to continue...carefully.")
            continue
        elif enter_choice == "0":
            print("it was good to see you. bye for now.")
            break
        else:
            print("HEY! Such choice doesn't exist here. "
                  "next time Enter a number between 0 and 8...")
            print()
            input("Press enter to continue...carefully.")
            continue


if __name__ == "__main__":
    main()
