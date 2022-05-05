import random


def generate_list():    # генерация списка
    el_count = random.randint(6, 15)
    lst = [random.randint(0, 9) for _ in range(el_count)]   # генератор списка с рандомными цифрами
    return lst

def get_longest_even_pos(lst):  # вычисление позиции начала самой длинной цепочки и его длины
    start = -1
    ln = 0      # длина наибольшей цепочки
    maxln = 0   # максимальная длинна цепочка
    maxst = -1  # позиция максимально длинной цепочки
    prev = 1    # элемент массива перед текущим
    for i, element in enumerate(lst):
        if element % 2 == 0:    # провДобавление / изменение необходимо реализовать минимум для 1 таблицы БД с внешними ключами.ерка на четность текущего элемента
            if prev % 2 == 0:   # проверка на четность предыдущего элемента
                ln += 1
            else:               # предыдущий не четный - задаем длину и стартовую позицию
                start = i
                ln = 1
            if ln > maxln:      # сли длина текущей цепочки больше, чем предыдущей - запоминаем
                maxln = ln
                maxst = start
        prev = element
    return maxst, maxln


def del_longest_even_num(lst): # удаление наибольшей цепочки
    s, ln = get_longest_even_pos(lst)
    for i in range(0, ln):
        del lst[s]
    return lst


def get_longest_even_pos_alternative(lst):  # вычисление позиции начала самой длинной цепочки и его длины без стандартных методов
    start = -1
    ln = 0      # длина наибольшей цепочки
    maxln = 0   # максимальная длинна цепочка
    maxst = -1  # позиция максимально длинной цепочки
    prev = 1    # элемент массива перед текущим
    i = 0
    for element in lst:
        if element % 2 == 0:    # провДобавление / изменение необходимо реализовать минимум для 1 таблицы БД с внешними ключами.ерка на четность текущего элемента
            if prev % 2 == 0:   # проверка на четность предыдущего элемента
                ln += 1
            else:               # предыдущий не четный - задаем длину и стартовую позицию
                start = i
                ln = 1
            if ln > maxln:      # сли длина текущей цепочки больше, чем предыдущей - запоминаем
                maxln = ln
                maxst = start
        prev = element
        i += 1
    return maxst, maxln

def del_longest_even_num_alternative(lst): # удаление наибольшей цепочки без стандартных методов
    s, ln = get_longest_even_pos_alternative(lst)
    result = []
    counter = 0
    for element in lst:
        if (counter < s) or (counter >= s+ln):
            result.append(element)
        counter += 1
    return result

if __name__ == '__main__':
    print("Желаете ввести список от руки или воспользоваться автоматической генерацией? (0 или 1)")
    while True:  # ввод, пока не будет корректным
        try:
            var = int(input())
            break
        except:
            print("Введенное значение - не число, попробуйте ещё раз")

    if var:
        lst = generate_list()
    else:
        while True:  # ввод, пока не будет корректным
            try:
                lst = list(map(int, input().split()))
                break
            except:
                print("Некорректный ввод")
    print("Введенный список:", lst)
    print("Список без самой длинной цепочки четных чисел", del_longest_even_num_alternative(lst))
