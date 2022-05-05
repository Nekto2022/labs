from pathlib import Path
import csv


def start_1(): # вывод кол-ва директорий в папке
    print("введите директорию")
    dir_name = input()
    dir = Path(dir_name)
    if dir.is_dir():
        folder_count = len([1 for file in dir.iterdir()]) # заполнение списка и подсчет его длины
        print(f"В папке {folder_count} файлов")
    else:
        print("Введенная строка не директория")

def start_2():
    with open("./test_data/data.csv") as f:
        data = csv.reader(f)    # считываем данные
        headers = next(data)
        dict_data = [dict(zip(headers, i)) for i in data]   # генератор для создания заголовков в качестве ключей словаря
        print("Данные в csv файле:", dict_data)
        return dict_data

def start_2_1(dict_data):
    sorted_dict_data = sorted(dict_data, key=lambda d: d['name']) # сортировка по имени
    print("Отсортированный список словарей (по имени):", sorted_dict_data)
    return sorted_dict_data

def start_2_2(dict_data):
    sorted_dict_data = sorted(dict_data, key=lambda d: d['N']) # сортировка по номеру
    print("Отсортированный список словарей (по номеру):", sorted_dict_data)
    return sorted_dict_data

def start_2_3(dict_data):
    dict_data = [element for element in dict_data if int(element['N']) > 2] # генератор списка словарей с N > 2
    print("список словарей, где N > 2:", dict_data)
    return dict_data

def save_csv(dict_data):
    with open("./test_data/new_data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(dict_data[0].keys()) # запись заголовков
        for item in dict_data:
            writer.writerow(item.values())  # запись строк


if __name__ == '__main__':
    start_1()
    dict = start_2()
    sorted_dict = start_2_1(dict)
    start_2_2(dict)
    start_2_3(dict)
    save_csv(sorted_dict)