Задание 1
from datetime import datetime, timedelta

def datetime_info(date_str):
    # Преобразуем строку в объект datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    ы
    # Форматируем дату в нужный формат
    formatted_date = date_obj.strftime('%d-%m-%Y')
    
    # Получаем день недели
    day_of_week = date_obj.strftime('%A')
    
    # Определяем количество дней до следующего года
    next_year = datetime(date_obj.year + 1, 1, 1)
    days_until_next_year = (next_year - date_obj).days
    
    # Собираем результаты в словарь
    result = {
        'formatted_date': formatted_date,
        'day_of_week': day_of_week,
        'days_until_next_year': days_until_next_year
    }
    
    return result

# Пример использования
date_info = datetime_info('2023-10-14')
print(date_info)

Задание 2

def write_and_read_file(filename, content):
    # Записываем строку в файл
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    
    # Считываем содержимое файла и возвращаем его
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Пример использования
result = write_and_read_file('example.txt', 'Hello, world!')
print(result)


Задание 3

import os

def list_files_in_directory(directory_path):
    # Получаем список всех файлов и подкаталогов в указанном каталоге
    entries = os.listdir(directory_path)
    
    # Фильтруем только файлы
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
    
    return files

# Пример использования
directory_path = '/path/to/your/directory'  # Замените на нужный путь
files = list_files_in_directory(directory_path)
print(files)

Задание 4

import os

def ensure_directory_exists(directory_path):
    # Проверяем, существует ли каталог
    if not os.path.exists(directory_path):
        # Если не существует, создаем его
        os.makedirs(directory_path)

# Пример использования
directory_path = '/path/to/your/directory'  # Замените на нужный путь
ensure_directory_exists(directory_path)

Задание 5

import os
import time

def file_stats(filepath):
    # Проверяем, существует ли файл
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    # Получаем размер файла
    file_size = os.path.getsize(filepath)
    
    # Получаем время последнего изменения
    last_modified_time = os.path.getmtime(filepath)
    last_modified = time.ctime(last_modified_time)  # Форматируем время
    
    # Получаем имя файла и его расширение
    file_name, file_extension = os.path.splitext(os.path.basename(filepath))
    
    # Собираем результаты в словарь
    stats = {
        'size': file_size,
        'last_modified': last_modified,
        'name': file_name,
        'extension': file_extension
    }
    
    return stats

# Пример использования
filepath = '/path/to/your/file.txt'  # Замените на нужный путь
try:
    stats = file_stats(filepath)
    print(stats)
except FileNotFoundError as e:
    print(e)



