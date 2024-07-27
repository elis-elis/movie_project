def read_template():
    with open('_static/index_template.html', 'r') as content:
        return content.read()


def generate_movie_info(movie_name, details):
    """
    Generates HTML for a single movie.
    """
    return f""" 
    <li class= movie"> 
        <img src="{details['poster_url']}" alt="{movie_name}">
        <div>
            <h2>{movie_name}</h2>
            <p><strong>Year</strong> {details['year']}</p>
            <p><strong>Rating</strong> {details['rating']}</p>
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



