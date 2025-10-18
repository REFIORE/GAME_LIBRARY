import os
import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('API_KEY')
    payload = {
        'key': token,
        'genres': 'strategy'
    }
    url = 'https://api.rawg.io/api/games'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    games = response.json()['results']

    for game in games:
        slug = game['slug']
        game_name = game['name']
        game_url = f'https://rawg.io/games/{slug}'
        date_released = game['released']
        print(f'Название игры: {game_name}')
        print(f'Дата выхода: {date_released}')
        print(f'Ссылка на игру: {game_url}\n')


if __name__ == "__main__":
    main()
