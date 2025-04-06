import numpy as np

class  MyMatrix:
    def __init__(self, n, f, s):
        self.__matrix = np.array(np.round(np.random.uniform(f, s, n*n)).reshape(n, n))
        self.__size = n

    def __str__(self): return str(self.__matrix)

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

    # C = A.makeC(B)
    # D = A.makeD(B)

    # C = (BT * A – AT * B) + (A – 6E)T / min | Bij |
    def makeC(self, B):
        t1 = ((np.transpose(B.__matrix) @ self.__matrix) -
              (np.transpose(self.__matrix) @ B.__matrix))

        t2 = (np.transpose(self.__matrix - 6*np.eye(self.__size)))/(B.__matrix.min())

        return t1 + t2

    # D = (A + B)^2 / max | Aij | - 8B^2
    def makeD(self, B):
        t1 = (self.__matrix + B.__matrix)**2
        t1 /= self.__matrix.max()
        return t1 - 8*B.__matrix**2

if __name__ == '__main__':
    m1_original = MyMatrix(5, 1, 10)
    m2_original = MyMatrix(7, -10, 10)

    m1_copy = m1_original
    print(m1_copy)
    print('-'*50)
    m1_copy.modify()
    print(m1_copy)

    print()

    m2_copy = m2_original
    print(m2_copy)
    print('-'*50)
    m2_copy.modify()
    print(m2_copy)

    print()
    print('#'*50)
    print()

    m3 = MyMatrix(3, 1, 5)
    m4 = MyMatrix(3, 6, 10)

    print(m3)
    print()
    print(m4)

    print()
    print()

    print(m3.makeC(m4))
    print()
    print(m3.makeD(m4))
