import math
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from collections.abc import Iterable

def EisenInt(a, b):
    return [a, b * (-1+np.sqrt(3))/2]

def gospOnce(p, a):
    newP = []
    newP.append(p*a)
    newP.append(p*a + EisenInt(1,0))
    newP.append(p*a + EisenInt(1,1))
    newP.append(p*a + EisenInt(0,1))
    newP.append(p*a + EisenInt(-1,0))
    newP.append(p*a + EisenInt(-1,-1))
    newP.append(p*a + EisenInt(0,-1))

    return newP

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

lst = [([0.37796447, 1.96396101], [2.26778684, 2.61861468]), ([2.26778684, 2.61861468], [3.77964473, 1.30930734]),
       ([3.77964473, 1.30930734], [1.88982237, 0.65465367]), ([1.88982237, 0.65465367], [ 1.51185789, -1.30930734]),
       ([ 1.51185789, -1.30930734], [ 3.40168026, -0.65465367]), ([ 3.40168026, -0.65465367], [5.29150262e+00, 8.88678020e-13]),
       ([5.29150262e+00, 8.88678020e-13], [5.6694671,  1.96396101])]

res = list(flatten(lst))
print(lst)
print(res)

currLogic = 'A'
currLogic = currLogic.replace('A', 'A-B--B+A++AA+B-')
print(currLogic)
v = [1,1]

x = [v[0]]
y= [v[1]]

fig, ax = plt.subplots()
ax.plot(x, y)

# Передвигаем левую ось Y и нижнюю ось X в центр, установив положение «центр»
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Устраняем верхнюю и правую оси, установив цвет сплайна «none»
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Выводим график
plt.show()






#             x1         y1                        x2                      y2
var = [((np.int64(0), np.int64(0)), (np.float64(-0.8660254037844385), np.float64(1.5))), ((np.int64(0), np.int64(0)), (np.float64(0.0), np.float64(2.0))), ((np.int64(0), np.int64(0)), (np.float64(0.0), np.float64(1.0))), ((np.int64(0), np.int64(0)), (np.float64(0.8660254037844385), np.float64(0.5))), ((np.int64(0), np.int64(0)), (np.float64(0.8660254037844385), np.float64(1.5))), ((np.int64(0), np.int64(0)), (np.float64(0.8661735217750571), np.float64(2.499948685508523))), ((np.int64(0), np.int64(0)), (np.float64(0.0), np.float64(3.0)))]

x = []
y = []
for vr in var:
    for j in range(len(vr)):
        if j == 0 or j == 2:
            x.append(vr[j])
        else:
            y.append(vr[j])

# Создаём область для построения графика и получаем фигуру и дескриптор осей в возвращённом объекте
fig, ax = plt.subplots()

# Строим данные на дескрипторе осей
ax.plot(x, y, 'o')

# Передвигаем левую ось Y и нижнюю ось X в центр, установив положение «центр»
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Устраняем верхнюю и правую оси, установив цвет сплайна «none»
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Выводим график
plt.show()


# def complement(path: str) -> str:
#     position = int(len(path) // 2)
#     path = path[:position] + str(abs(int(path[int(len(path) // 2)]) - 1)) + path[position + 1:]
#     return path
#
#
# def generate_dragon(scale, order):
#     path = "1"
#     i = 1
#     while i <= order:
#         path = path + "1" + complement(path)
#         i += 1
#     points = [(0, 0)]
#     angle = 0
#     for p in path:
#         if p == "1":
#             angle = angle + math.pi / 2
#         else:
#             angle = angle - math.pi / 2
#         x = points[-1][0] - scale * math.cos(angle)
#         y = points[-1][1] - scale * math.sin(angle)
#         points.append((x, y))
#     return points
#
# SCALE = 10
# order = 12
#
# points = generate_dragon(SCALE, order)
# X = [j[0] for j in points]
# Y = [j[1] for j in points]
# fig, ax = plt.subplots(figsize=(10, 10))
#
# plt.plot(X, Y)
# ax.set_aspect('equal', adjustable='box')
# plt.show()