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

