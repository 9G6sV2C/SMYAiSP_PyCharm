from tkinter import *
import threading
import queue
import random, time
import numpy as np

colors = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white", "grey"]
i = 0  # глобальный счетчик числа потоков



# графический компонент для рисования овалов
class ThreadGUI(Canvas):
    def __init__(self, parent = None):
        Canvas.__init__(self, parent)
        self.__dataQueue = queue.Queue() # получаем ссылку на очередь
        self.consumer() # вызываем метод-потребитель, чтобы сразу при создании компоненета читать из очереди

    def producer(self, color): # производитель - что делает наш поток
        print("producer")
        while True:
            time.sleep(1) # усыпляем на 2 секунды
            self.__dataQueue.put(color, True) # блокирующая запись

    def consumer(self): # потребитель
        print("consumer")
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
    global i, colors
    while i < numOfThrds:
        color = colors[i % len(colors)]
        threading.Thread(target=widget.producer, args=(color, )).start()
        print(i, "->", color)
        i += 1

if __name__ == '__main__':
    root = Tk()
    widget = ThreadGUI(root)

    widget.pack(side=TOP, expand=YES, fill=BOTH)

    CreateThreads(widget, 2)

    root.mainloop()
