import os
import re

# Укажите путь к каталогу
directory = 'photos'

# Получаем список всех файлов в каталоге
files = os.listdir(directory)

# Функция для извлечения номера из имени файла
def get_number(file_name):
    match = re.search(r'image_(\d+)_pixelbin\.jpeg', file_name)
    if match:
        return int(match.group(1))
    return None

# Сортируем файлы по извлеченному номеру
sorted_files = sorted(files, key=get_number)

# Счетчик для новых имен
counter = 1

# Обходим все файлы в отсортированном списке
for file_name in sorted_files:
    # Проверяем, является ли текущий элемент файлом и соответствует ли его имя формату image_X_pixelbin.jpeg
    if os.path.isfile(os.path.join(directory, file_name)) and file_name.startswith('image_') and file_name.endswith('_pixelbin.jpeg'):
        # Формируем новое имя файла с трехзначным номером
        new_name = f'IMG_{counter:03}.jpeg'
        # Путь к старому файлу
        old_path = os.path.join(directory, file_name)
        # Путь к новому файлу
        new_path = os.path.join(directory, new_name)
        # Переименовываем файл
        os.rename(old_path, new_path)
        # Увеличиваем счетчик
        counter += 1

print('Переименование завершено.')
