from tkinter import *
import threading
import queue
import random, time
import numpy as np

colors = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white", "grey"]
# i = 0  # глобальный счетчик числа потоков
canvas_width = 600
canvas_height = 600

class MatrixColor(Canvas):
    def __init__(self, parentWindow = None):
        Canvas.__init__(self, parentWindow)
        self.__threadQueue = queue.Queue()

    # производитель - действия потока
    def producer(self):
        print("producer")
        selectedColor = colors[np.random.randint(0,8)]

        matrix = np.zeros((128, 128))

        # Выбор закрашиваемых клеток
        for i in range(128):
            for j in range(128):
                matrix[i][j] = np.random.randint(0,1)

        while True:
            time.sleep(2)
            self.__threadQueue.put((selectedColor, matrix), True)

        # for i in range(10):
        #     time.sleep(1) # усыпляем на 2 секунды
        #     self.__dataQueue.put(color, True) # блокирующая запись

    # потребитель
    def consumer(self):
        print("consumer")
        try:
            currColor, currMatrix = self.__threadQueue.get(False) # неблокирующее чтение
        except queue.Empty:
            pass
        else:
            cell_width = canvas_width / 128
            cell_height = canvas_height / 128

            for i in range(128):
                for j in range(128):
                    if currMatrix[i][j] == 1:  # Рисуем только клетки со значением 1
                        x1 = col * cell_width
                        y1 = row * cell_height
                        x2 = x1 + cell_width
                        y2 = y1 + cell_height
                        canvas.create_rectangle(x1, y1, x2, y2, outline='white', fill='red', width=4)

            self.after(100, self.consumer)  # Повторяем проверку очереди


# графический компонент для рисования овалов
class ThreadGUI(Canvas):
    def __init__(self, parent = None):
        Canvas.__init__(self, parent)
        self.__dataQueue = queue.Queue() # получаем ссылку на очередь
        self.consumer() # вызываем метод-потребитель, чтобы сразу при создании компоненета читать из очереди

    def producer(self, color): # производитель - что делает наш поток
        for i in range(10):
            time.sleep(1) # усыпляем на 2 секунды
            self.__dataQueue.put(color, True) # блокирующая запись

    def consumer(self): # потребитель
        try:
            color = self.__dataQueue.get(False) # неблокирующее чтение
        except queue.Empty:
            pass
        else:
            self.create_oval(random.randint(1,20), random.randint(1,20),
                             random.randint(80,250), random.randint(80, 250),
                             outline = color, fill = color, width = 2)
        self.after(100, self.consumer) # отложенный вызов # 1000


# здесь будем создавать потоки
def CreateThreads(widget, numOfThrds):
    for i in range(numOfThrds):
        threading.Thread(target=widget.producer).start()



    # global i, colors
    # while i < numOfThrds:
    #     color = colors[i % len(colors)]
    #     threading.Thread(target=widget.producer, args=(color, )).start()
    #     print(i, "->", color)
    #     i += 1

if __name__ == '__main__':
    root = Tk()
    widget = MatrixColor(root)

    widget.pack(side=TOP, expand=YES, fill=BOTH)

    CreateThreads(widget, 2)

    root.mainloop()
