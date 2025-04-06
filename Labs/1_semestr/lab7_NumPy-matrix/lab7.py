import numpy as np

class  MyMatrix:
    def __init__(self, n, f, s):
        self.__matrix = np.array(np.round(np.random.uniform(f, s, n*n)).reshape(n, n))
        self.__size = n

    def __str__(self): return str(self.__matrix)

    def getMin(self): return self.__matrix.min()
    def getMax(self): return self.__matrix.max()

    # найти максимальный элемент и поставить его на первое место.
    def modify(self):
        tempM = np.transpose(self.__matrix)

        for row in tempM:
            row[0] = np.max(row)

        self.__matrix = np.transpose(tempM)

    # C = A.makeC(B)
    # D = A.makeD(B)

    # C = (BT * A – AT * B) + (A – 6E)T / min | Bij |
    def makeC(self, B):
        t1 = ((np.transpose(B.__matrix) @ self.__matrix) -
              (np.transpose(self.__matrix) @ B.__matrix))

        t2 = (np.transpose(self.__matrix - 6*np.eye(self.__size)))/(B.getMin())

        return t1 + t2

    # D = (A + B)^2 / max | Aij | - 8B^2
    def makeD(self, B):
        t1 = (self.__matrix + B.__matrix)**2
        t1 /= self.getMax()
        return t1 - 8*B.__matrix**2

if __name__ == '__main__':
    m1 = MyMatrix(5, 1, 10)
    m1_copy = m1
    m2 = MyMatrix(5, 1, 10)
    m2_copy = m2

    print(m1_copy)
    print('-'*40)
    m1_copy.modify()
    print(m1_copy)

    print()
    print()

    print(m2_copy)
    print('-' * 40)
    m2_copy.modify()
    print(m2_copy)

    print()
    print()

    print(m1.makeC(m2))
    print(m1.makeD(m2))

