from random import choice
import movie_storage
import requests


API_KEY = '5ed97f7c'
OMDb_API = 'http://www.omdbapi.com/?i=tt3896198&apikey=5ed97f7c'

""" Send all data requests to: 'http://www.omdbapi.com/?apikey=[yourkey]&' 
"""


def display_menu():
    """
        Display the main menu with options for the user.
    """
    print()
    print("°°°°°°°°°° Salut, here's E's movies database °°°°°°°°°°")
    print()
    print("Check out the Menu:")
    print()
    print("0. if you wish to exit - this is the way to go")
    print("1. (very straightforward) it's a List of movies")
    print("2. you can Add movie(s) here")
    print("3. Say goodbye to a movie or Delete it")
    print("4. Update movie(s), if you have to")
    print("5. yeap, Stats (just FYI)")
    print("6. Random movie --> for a spontaneous evening")
    print("7. Search movie, like a detective ;)")
    print("8. Movies sorted by rating (again very straightforward stuff)")
    print()


def list_movies():
    """
        List all movies in the database with their ratings.
    """
    movies = movie_storage.load_movies()
    total_movies = 0
    for movie, rating in movies.items():
        total_movies += 1
    print(f"{total_movies} movies in total here.")
    for movie, details in movies.items():
        print(f"{movie}, year of release is {details['year']}, "
              f"and rating is {details['rating']}")


def add_movie():
    """
        Adds a movie to the movies database
    """
    # Get the data from the JSON file
    movies = movie_storage.load_movies()
    try:
        title = input("Guess what. You can enter a movie name here: ")
        year = int(input("... now enter a year of release here: "))
        rating = float(input("... and now enter a rating for this movie: "))
        if title in movies:
            print(f"Ah! Look at that - movie {title} already exist!")

        if 1 <= rating <= 10:
            movie_storage.add_movie(title, year, rating)
            print(f"Voila! Movie {title} was added successfully.")
        else:
            print("Oops, your rating can't be accepted, "
                  "please check your input to be a number between 1 and 10. ;) ")
    except ValueError as error:
        print("Oh nooo! That will not work here. "
              "Please enter a valid number for the rating.", error)


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


def movie_statistics():
    """
        Display statistics about the movies in the database,
        including average rating, median rating,
        best movie by rating, and worst movie by rating.
    """
    movies = movie_storage.load_movies()

    # Average rating
    ratings = []
    for details in movies.values():
        ratings.append(details['rating'])
    average_movie_rating = sum(ratings) / len(ratings)
    print("Average rating:", average_movie_rating)

    # Median rating
    sorted_ratings = sorted(ratings)
    length = len(sorted_ratings)
    if length % 2 == 0:
        median_movie_rating = (sorted_ratings[(length) // 2] + sorted_ratings[(length) // 2 - 1]) / 2
    else:
        median_movie_rating = sorted_ratings[length // 2]
    print("Median rating:", median_movie_rating)

    # best movie:
    best_movie = max(movies.items(), key=lambda movie: movie[1]['rating'])
    print(f"Best movie(s): {best_movie[0]}, Rating {best_movie[1]['rating']}")

    # The worst movie by rating
    worst_movie = min(movies.items(), key=lambda movie: movie[1]['rating'])
    print(f"Worst movie: {worst_movie[0]}, Rating {worst_movie[1]['rating']}")


def random_movie():
    """
        Select a random movie from the database and display its title and rating.
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
    query = input("Enter part of movie name: ").lower()
    # Convert the query to lowercase for case-insensitive search
    for movie, details in movies.items():
        # Convert the movie name to lowercase for case-insensitive search
        movie_lower = movie.lower()
        # Check if the query is a substring of the movie name
        if query in movie.lower():
            print(f"{movie}, its year of release: {details['year']}, "
                  f"and it's rated: {details['rating']}.")


def movies_sorted_by_rating():
    """
        Sort and display the movies in the database by rating in descending order.
    """
    movies = movie_storage.load_movies()
    sorted_movies = sorted(movies.items(), key=lambda r: r[1]['rating'], reverse=True)
    for movie, details in sorted_movies:
        print(f"{movie}, its year of release: {details['year']}, "
              f"and it's rated: {details['rating']}.")


def main():
    """
       Main function to run the movie database application.
    """
    # this line starts an infinite loop. It will continue running until it is terminated
    while True:
        # call function to print the menu options
        display_menu()
        enter_choice = input("and now you may Enter your choice (0-8): ")
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
        elif enter_choice == "0":
            print("it was good to see you. bye for now.")
            break
        else:
            print("HEY! Such choice doesn't exist here. "
                  "next time Enter a number between 1 and 8...")
            print()
            input("Press enter to continue...carefully.")
            continue


if __name__ == "__main__":
    main()
