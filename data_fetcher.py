import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(movie_name):
    api_url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            return data
        else:
            print("No data found for the movie:", movie_name)
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None


movie_name = "Clerks"
movie_data = fetch_data(movie_name)
if movie_data:
    print("Movie Data:", movie_data)
else:
    print("Failed to fetch data for the movie:", movie_name)
