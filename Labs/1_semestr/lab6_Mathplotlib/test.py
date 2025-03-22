import numpy as np
import matplotlib.pyplot as plt
from tkinter.colorchooser import askcolor

s = ''
with open('test.txt', 'r') as f:
    temp = f.readline()
    s += temp

    temp = f.readline()
    s += temp

    temp = f.readline()
    s += temp

    temp = f.readline()
    s += temp

    temp = f.readline()
    s += temp

    temp = f.readline()
    s += temp

    f.close()

with open('test_write.txt', 'w') as f2:

    f2.write('666')

    f2.close()
print(s)

# Параметр a для масштабирования
a = 1

# Параметр t от 0 до 2π
t = np.linspace(0, 2 * np.pi, 1000)

# Параметрические уравнения дельтоиды
x = a * (2 * np.cos(t) + np.cos(2 * t))
y = a * (2 * np.sin(t) - np.sin(2 * t))

# Настройка графика
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Дельтоида', color='b')
plt.title('Дельтоида')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
