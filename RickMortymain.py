import requests
import json
import random

# Базовый URL API
BASE_URL = "https://rickandmortyapi.com/api"

# Функция для получения информации о случайном персонаже
def get_random_character():
    # Получение общего количества персонажей
    response = requests.get(f"{BASE_URL}/character")
    data = response.json()
    total_characters = data['info']['count']
    
    # Выбор случайного ID персонажа
    random_id = random.randint(1, total_characters)
    response = requests.get(f"{BASE_URL}/character/{random_id}")
    
    # Проверка ответа и вывод данных
    if response.status_code == 200:
        character_data = response.json()
        print(f"Случайный персонаж: {character_data['name']}")
        print(f"Статус: {character_data['status']}")
        print(f"Вид: {character_data['species']}")
        print(f"Место происхождения: {character_data['origin']['name']}")
    else:
        print("Не удалось получить информацию о персонаже")

# Функция для поиска персонажей по имени
def search_character_by_name(name):
    response = requests.get(f"{BASE_URL}/character/?name={name}")
    
    if response.status_code == 200:
        characters = response.json()['results']
        for char in characters:
            print(f"Имя: {char['name']}, Статус: {char['status']}, Вид: {char['species']}")
    else:
        print("Персонаж не найден")

# Функция для получения списка всех локаций
def get_all_locations():
    response = requests.get(f"{BASE_URL}/location")
    
    if response.status_code == 200:
        data = response.json()
        for location in data['results']:
            print(f"Локация: {location['name']}, Тип: {location['type']}, Измерение: {location['dimension']}")
    else:
        print("Не удалось получить список локаций")

# Функция для поиска эпизодов по названию
def search_episode_by_name(name):
    response = requests.get(f"{BASE_URL}/episode/?name={name}")
    
    if response.status_code == 200:
        episodes = response.json()['results']
        for ep in episodes:
            print(f"Название: {ep['name']}, Дата выхода: {ep['air_date']}, Эпизод: {ep['episode']}")
    else:
        print("Эпизод не найден")

# Пример использования функций
if __name__ == "__main__":
    print("Получение случайного персонажа:")
    get_random_character()
    
    print("\nПоиск персонажа по имени:")
    search_character_by_name("Rick")

    print("\nПолучение списка всех локаций:")
    get_all_locations()

    print("\nПоиск эпизодов по названию:")
    search_episode_by_name("Pilot")
