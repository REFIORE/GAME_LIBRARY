import os
import requests
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('API_KEY')
payload = {
    'key': token,
}
url = 'https://api.rawg.io/api/games'
response = requests.get(url, params=payload)
response.raise_for_status()
response = response.json()

game_name = response['results']['name']

print('Название игры: ', game_name)
