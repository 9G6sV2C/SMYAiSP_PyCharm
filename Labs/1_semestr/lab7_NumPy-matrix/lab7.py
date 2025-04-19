import numpy as np

# В конструкторе матрица булет пустая,
# Сделать отдельный метод запления случ. числавм
# Сделать метод ввода матрицы с клавиатуры
class  MyMatrix:
    def __init__(self, rows, cols):
        # self.__matrix = np.array(np.round(np.random.uniform(A, B, n*n)).reshape(n, n))
        self.__matrix = np.empty([rows, cols])
        self.__rows = rows
        self.__cols = cols

    def __str__(self): return str(self.__matrix)

    # Заполнение случайными числами
    def fillRandom(self, A, B):
        self.__matrix[:, :] = np.random.randint(A, B+1, size=(self.__rows, self.__cols))

    def inputMatrix(self):
        while True:
            matrix = []
            print(f"\nВведите матрицу {self.__rows}x{self.__cols} (целые числа, разделённые пробелами, "
                  f"каждая строка с новой строки):")
            try:
                for i in range(self.__rows):
                    while True:
                        # .strip() - убрать пробелы в начале и конце строки
                        rows_input = input(f"Строка {i + 1}: ").strip()
                        elements = rows_input.split()

                        if len(elements) != self.__cols:
                            print(f"Ожидается {self.__cols} элементов в строке. Вы ввели {len(elements)}. Попробуйте снова.")
                            continue

                        try:
                            row = list(map(int, elements))
                            matrix.append(row)
                            break
                        except ValueError:
                            print("Все элементы должны быть целыми числами. Попробуйте снова.")

                self.__matrix[:, :] = np.array(matrix)
                return

            except ValueError:
                print("Пожалуйста, введите целое число для размеров матрицы. Попробуйте снова.")

    # найти максимальный элемент в столбце и поставить его на первое место.
    def modify(self):
        # транспонируем для более удобного обхода
        tempM = np.transpose(self.__matrix)

        for row in tempM:
            maxIndex = np.argmax(row)
            temp = row[0]
            row[0] = row[maxIndex]
            row[maxIndex] = temp

        # транспонируем обратно
        tempM = np.transpose(tempM)

        self.__matrix = tempM

    # Вызов должен выглядеть так
    # C = A.makeC(B)
    # D = A.makeD(B)

    # C = (BT * A – AT * B) + (A – 6E)T / min | Bij |
    # Только квадратные матрицы одинаково размера
    def makeC(self, B):
        try:
            t1 = ((np.transpose(B.__matrix) @ self.__matrix) -
                  (np.transpose(self.__matrix) @ B.__matrix))

            t2 = ((np.transpose(self.__matrix - 6*np.eye(self.__rows, self.__cols)))/
                  (B.__matrix.min()))

            return t1 + t2

        except ValueError as ve:
            print(f"Ошибка в makeC: {ve}")
            print(f"Размер матрицы self: {self.__rows} на {self.__cols}")
            print(f"Размер матрицы B: {B.__rows} на {B.__cols}")
            return None

    # D = (A + B)^2 / max | Aij | - 8B^2
    # Только квадратные матрицы одинаково размера
    def makeD(self, B):
        try:
            t1 = (self.__matrix + B.__matrix)**2
            t1 /= self.__matrix.max()
            return t1 - 8 * B.__matrix**2

        except ValueError as ve:
            print(f"Ошибка в makeD: {ve}")
            print(f"Размер матрицы self: {self.__rows} на {self.__cols}")
            print(f"Размер матрицы B: {B.__rows} на {B.__cols}")
            return None

    def __add__(self, other):
        try:
            return self.__matrix + other.__matrix
        except ValueError as ve:
            print(f"Ошибка сложения матриц: {ve}")


if __name__ == '__main__':
    mm1 = MyMatrix(3, 5)
    mm1.inputMatrix()

    m1_original = MyMatrix(4, 4)
    m2_original = MyMatrix(4, 4)

    m1_original.fillRandom(1, 10)
    m2_original.fillRandom(1, 99)

    print(m1_original)
    print()
    print(m2_original)
    print()

    print("Сложение:")
    print(m1_original + m2_original)
    print()

    print('-'*50)
    print()

    m1_copy = m1_original
    m1_copy.modify()
    print("m1_copy.modify():")

    print(m1_copy)
    print()

    print('-'*25)
    print()

    m2_copy = m2_original
    print("m2_copy.modify():")
    m2_copy.modify()
    print(m2_copy)

    print()
    print('#'*50)
    print()

    m3 = MyMatrix(4, 4)
    m4 = MyMatrix(4, 4)

    m3.fillRandom(1, 10)
    m4.fillRandom(1, 99)

    print(m3)
    print()
    print(m4)

    print()

    print("m3.makeC(m4):")
    print(m3.makeC(m4))
    print()
    print("m3.makeD(m4):")
    print(m3.makeD(m4))
