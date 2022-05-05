import random
import string
from pathlib import Path
import csv


class CSVFile:
    '''
    Класс отвественный за работу с файлами.
    input_file - путь к csv файлу откуда берутся данные
    output_file - путь к файлу куда необходимо сохранить данные
    '''
    def __init__(self, input_file, output_file, *args, **kwargs):
        self.input_file = input_file
        self.output_file = output_file

    @staticmethod
    def count_files(directory):
        directory = Path(directory)
        if directory.is_dir():
            folder_count = len([1 for file in directory.iterdir()])  # заполнение списка и подсчет его длины
            print(f"В папке {folder_count} файлов")
        else:
            print("Введенная строка не директория")
            folder_count = -1
        return folder_count

    def write_to_csv(self, list_dict_data=None, output_file=None):
        if list_dict_data is None:
            return None
        if output_file is None:
            output_file = self.output_file
        with open(output_file, "w") as f:
            writer = csv.writer(f)
            writer.writerow(list_dict_data.keys())  # запись заголовков
            for item in list_dict_data:
                writer.writerow(item.values())  # запись строк
        return output_file

    def read_csv(self, filename=None):
        if filename is None:
            filename = self.input_file
        with open(filename) as f:
            data = csv.reader(f)  # считываем данные
            headers = next(data)
            dict_data = [dict(zip(headers, i)) for i in
                         data]  # генератор для создания заголовков в качестве ключей словаря
            print("Данные в csv файле:", dict_data)
        return dict_data


class Students(CSVFile):
    '''
    Класс ответственный за работу со структурой данных студентов
    input_file - путь к csv файлу откуда берутся данные
    output_file - путь к файлу куда необходимо сохранить данные
    data_frame - опциональный аргумент, структура данных (по умолчанию берется из input_file)
    '''
    def __init__(self, input_file, output_file, data_frame=None, *args, **kwargs):
        super().__init__(input_file, output_file)
        if data_frame is None:
            self.data_frame = self.read_csv(input_file)

    def sort_by_n(self):
        return sorted(self.data_frame, key=lambda d: d['N'])

    def sort_by_name(self):
        return sorted(self.data_frame, key=lambda d: d['name'])

    def sort_by_n_more_then(self, N):
        return [element for element in self.data_frame if int(element['N']) > N]

    def __getitem__(self, item):
        return [element[item] for element in self.data_frame]

    def __iter__(self):
        self.counter = -1
        self.limit = len(self.data_frame) - 1
        return self

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        else:
            self.counter += 1
            return self.data_frame[self.counter]

    def __str__(self):
        return f"Students: {self.data_frame}"

    @staticmethod
    def data_generator():
        while True:
            n = random.randint(0, 999999)
            name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(0,9)))
            email = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(0,9))) + '@mail.ru'
            group = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(0,4)))
            yield {'n': n, 'name': name, 'email': email, 'group': group}


if __name__ == '__main__':
    Students.count_files('./')
    st = Students('./test_data/data.csv', './test_data/new_data.csv')
    print("Отсортированный список словарей (по имени):", st.sort_by_name())
    print("Отсортированный список словарей (по номеру):", st.sort_by_n())
    print("список словарей, где N > 1:", st.sort_by_n_more_then(1))