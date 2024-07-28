trailer_links = {
    "Control": "https://www.youtube.com/watch?v=xUz6y6ANIgE",
    "Clerks": "https://www.youtube.com/watch?v=Mlfn5n-E2WE",
    "La haine": "https://www.youtube.com/watch?v=OfE0o9B3dhI",
    "Eraserhead": "https://www.youtube.com/watch?v=7WAzFWu2tVw",
    "The Aerial": "https://www.youtube.com/watch?v=Jr4SiSeSzTI",
    "The Man Who Wasn't There": "https://www.youtube.com/watch?v=htxvLcSnOU0",
    "American History X": "https://www.youtube.com/watch?v=LZGVcd5clgg",
    "Frances Ha": "https://www.youtube.com/watch?v=YdxCnCvCngk",
    "Following": "https://www.youtube.com/watch?v=62TTN6gD2So",
    "To Kill a Mockingbird": "https://www.youtube.com/watch?v=KR7loA_oziY",
    "Psycho": "https://www.youtube.com/watch?v=DTJQfFQ40lI",
    "Casablanca": "https://www.youtube.com/watch?v=66Zvg0YW870"
}


def read_template():
    with open('_static/index_template.html', 'r') as content:
        return content.read()


def generate_movie_info(movie_name, details):
    """
    Generates HTML for a single movie.
    """
    trailer_url = trailer_links.get(movie_name)
    trailer_html = f'<a class="trailer-link" href="{trailer_url}" target="_blank">trailer</a>' \
        if trailer_url else '<p class="trailer-coming-soon">trailer is not here, yet</p>'
    return f""" 
    <li> 
        <div class="movie">
            <img class="movie-poster" src="{details['poster_url']}" alt="{movie_name}">
            <h2 class="movie-title">{movie_name}</h2>
            <p class="movie-year">Year <strong>{details['year']}</strong></p>
            <p class="movie-rating">Rating <strong>{details['rating']}</strong></p>
            {trailer_html}
        </div>
    </li>
    """


def generate_movies_info(data):
    """
    Generates HTML for all movies in the database.
    """
    output = ""
    if data:
        for movie_name, details in data.items():
            output += generate_movie_info(movie_name, details)
    else:
        print("nothing is here")
    return output


def write_to_html_file(content):
    """
    Writes the final HTML content to the index.html file.
    """
    with open('_static/movies.html', 'w') as new_file:
        return new_file.write(content)
