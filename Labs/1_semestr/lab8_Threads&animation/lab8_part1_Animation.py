from tkinter import *
import threading
import queue
import random
import time
import numpy as np
from typing import Tuple, List

# Константы вынесены в отдельный блок
COLORS = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "grey"]
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
MATRIX_SIZE = 10  # Размер матрицы
UPDATE_INTERVAL_MS = 1000  # Интервал обновления холста в миллисекундах
THREAD_SLEEP_TIME = 2  # Время сна потока в секундах


class MatrixColor(Canvas):
    def __init__(self, parent_window: Tk = None):
        super().__init__(parent_window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.__thread_queue = queue.Queue()
        self.__running = True  # Флаг для управления потоками
        self.consumer()  # Запускаем потребитель

    def producer(self, thread_id: int):
        """Поток заполняет матрицу и отправляет данные в очередь"""
        selected_color = COLORS[thread_id % len(COLORS)]  # Цвет зависит от ID потока
        matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=int)  # Изначально нулевая матрица

        while self.__running:
            # Выбираем случайную позицию в матрице
            i, j = random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1)
            matrix[i][j] = 1  # Устанавливаем точку

            # Отправляем текущее состояние в очередь
            self.__thread_queue.put((selected_color, i, j))

            time.sleep(THREAD_SLEEP_TIME)

    def consumer(self):
        """Обработка данных из очереди и отрисовка на холсте"""
        try:
            while True:
                # Получаем все доступные элементы из очереди
                color, i, j = self.__thread_queue.get_nowait()

                # Рассчитываем координаты прямоугольника
                cell_width = CANVAS_WIDTH / MATRIX_SIZE
                cell_height = CANVAS_HEIGHT / MATRIX_SIZE

                x1 = j * cell_width
                y1 = i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                # Рисуем точку (без очистки всего холста)
                self.create_rectangle(x1, y1, x2, y2,
                                      outline='black',
                                      fill=color,
                                      width=1)
        except queue.Empty:
            pass

        if self.__running:
            self.after(UPDATE_INTERVAL_MS, self.consumer)

    def stop(self):
        """Остановка всех потоков и потребителя"""
        self.__running = False


def create_threads(widget: MatrixColor, num_threads: int):
    """Создание и запуск потоков"""
    for i in range(num_threads):
        thread = threading.Thread(target=widget.producer, args=(i,))
        thread.daemon = True  # Потоки завершатся при завершении main
        thread.start()


if __name__ == '__main__':
    root = Tk()
    widget = MatrixColor(root)
    widget.pack(side=TOP, expand=YES, fill=BOTH)

    try:
        create_threads(widget, 4)
        root.mainloop()
    finally:
        widget.stop()  # Корректная остановка при закрытии окна