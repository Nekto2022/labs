import numpy as np

if __name__ == '__main__':
    n, m = 4, 5                   # задаем размер матрицы
    a = np.random.random((n,m))   # генерация матрицы
    b = np.abs(a).sum(axis=0)     # вычисляем сумму абсолютных значений столбцов
    print(a)                      # выводим матрицу
    print(min(a[:, b.argmax()]))  # выводим наибольший элемент столбца матрицы
