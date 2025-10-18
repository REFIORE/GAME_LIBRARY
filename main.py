import os
import requests
from dotenv import load_dotenv


def get_games():
    token = os.getenv('API_KEY')
    payload = {
        'key': token,
        'genres': 'strategy',
        'page_size': 10,
        'metacritic': 100,
        'tags': 'multiplayer',
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
        print(f'\nНазвание игры: {game_name}')
        print(f'Дата выхода: {date_released}')
        print(f'Ссылка на игру: {game_url}')

        screenshots_url = f'https://api.rawg.io/api/games/{slug}/screenshots'
        response = requests.get(screenshots_url, params=payload)
        response.raise_for_status()
        sceens = response.json()['results']
        print('Скриншоты из игры: ')
        for screen in sceens:
            screenshot = screen['image']
            print(screenshot)

        sell_url = f'https://api.rawg.io/api/games/{slug}/stores'
        response = requests.get(sell_url, params=payload)
        response.raise_for_status()
        sells = response.json()['results']
        print('Где можно приобрести: ')
        for sell in sells:
            sell_urls = sell['url']
            print(sell_urls)


def main():
    load_dotenv()
    get_games()


if __name__ == "__main__":
    main()
