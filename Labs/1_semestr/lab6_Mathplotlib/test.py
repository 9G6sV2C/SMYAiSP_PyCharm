import numpy as np
import matplotlib.pyplot as plt
from tkinter.colorchooser import askcolor

print(3.3 * np.array([1,2,3]))

print(askcolor())

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
