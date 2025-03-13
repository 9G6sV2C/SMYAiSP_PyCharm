import turtle
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from collections.abc import Iterable


from numpy.ma.core import arccos


def transfVec(vector, angle, new_length):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # Поворачиваем вектор
    rotated_vector = rotation_matrix @ vector

    # Находим текущую длину вектора
    current_length = np.linalg.norm(rotated_vector)

    # Устанавливаем новую длину
    if current_length != 0:
        scale_factor = new_length / current_length
        final_vector = rotated_vector * scale_factor
    else:
        final_vector = np.array([0, 0])

    return tuple(final_vector)

def rotateDot(vector, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    rotated_vector = rotation_matrix @ vector

    return rotated_vector

def getRotateAngle():
    # v1 = thirdApex(DivSegmInRatio(2 / 1, ((0,0),(step,0))), (0,step))
    # phi = np.arccos(
    #     ()/
    #     ()
    # )
    return 0.333473172252 # (в радианах) вычеслен в desmos экперементально

# ф-я нахождения коорд. k-ой части отрезка
def DivSegmInRatio(k, *ps): # ps -> ( (x1, y1), (x2, y2)) )
    return ((ps[0][0] + k*ps[1][0])/(1+k), (ps[0][1] + k*ps[1][1])/(1+k))

# ф-я нахождения коорд. 3-ей вершины в правильном треугольнике по 2 другим
def thirdApex(*points): # points -> ( (x1, y1), (x2, y2)) )
    xp = points[1][0] - points[0][0]
    yp = points[1][1] - points[0][1]
    x3 = points[0][0] + 0.5 * (xp - yp * np.sqrt(3))
    y3 = points[0][1] + 0.5 * (xp * np.sqrt(3) + yp)
    return (x3, y3)

# R or L
def getOrent(*points): # points -> ( (x1, y1), (x2, y2)) )
    if (points[1][0] - points[0][0]) * (points[1][1] - points[0][1]) > 0:
        return 'R'
    else:
        return 'L'

def ReflectAxes(points):
    newP = []
    for el in points:
        newP.append(((el[1]), el[0]))
    return newP

def ReverseLines(points):
    newP = []
    for i in range(len(points)-1, -1, -1):
        newP.append((points[i][0], points[i][1]))
    return newP

    return newP

'''
def gosperOnce_V2(arrLines, arrType, arrOrientation, order):
    if order == 0:
        return arrLines
    else:
        finalConv = []
        finalRule = ''
        finalOrent = ''
        # массив прямых, каждая из которых задаётся 2 точками,
        # каждая из которых задаётся 2 координатами
        # ТИП B - ЭТО ДВАЖДЫЕ ОТРАЖЁННЫЙ ТИП А
        for (currLine, currType, currOrent) in zip(arrLines, arrType, arrOrientation):
            newConv = []
            newRule = ''
            newOrnt = ''
            isRight = True
            pp = []

            p1 = thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine))
            p2 = thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine))
            p3 = DivSegmInRatio(2 / 1, *currLine)
            p4 = DivSegmInRatio(1 / 2, *currLine)
            p5 = thirdApex(DivSegmInRatio(1 / 2, *currLine), currLine[0])
            p6 = thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine))
            p7 = thirdApex(currLine[1], p3)
            p8 = currLine[1]

            pp.append(p1)
            pp.append(p2)
            pp.append(p3)
            pp.append(p4)
            pp.append(p5)
            pp.append(p6)
            pp.append(p7)
            pp.append(p8)

            if currType == 'A' and currOrent == 'R':
                for i in range(1, len(pp)):
                    newConv.append((pp[i-1], pp[i]))
                # newConv.append((p1, p2))
                # newConv.append((p2, p3))
                # newConv.append((p3, p4))
                # newConv.append((p4, p5))
                # newConv.append((p5, p6))
                # newConv.append((p6, p7))
                # newConv.append((p7, p8))
                newRule = 'ABBAAAB'
                newOrnt = 'RRLLRRR'
            elif currType == 'A' and currOrent == 'L':
                for i in range(len(pp)-1, -1, -1):
                    newConv.append((pp[i], pp[i-1]))
                # newConv.append((p1, p2))
                # newConv.append((p2, p3))
                # newConv.append((p3, p4))
                # newConv.append((p4, p5))
                # newConv.append((p5, p6))
                # newConv.append((p6, p7))
                # newConv.append((p7, p8))
                newRule = 'ABBAAAB'
                newOrnt = 'LLLRRLL'
            elif currType == 'B' and currOrent == 'R':
                pp_temp = ReflectAxes(*pp)
                for i in range(1, len(pp_temp)):
                    newConv.append((pp_temp[i-1], pp_temp[i]))
                newRule = 'ABBBAAB'
                newOrnt = 'RRRLLRR'
            elif currType == 'B' and currOrent == 'L':
                pp_temp = ReflectAxes(*pp)
                for i in range( len(pp_temp)-1, -1, -1):
                    newConv.append((pp_temp[i], pp_temp[i-1]))
                newRule = 'ABBBAAB'
                newOrnt = 'LLLRRLL'

            # if currOrent == 'L':
            #     currLine = ((currLine[1][0],currLine[1][1]),(currLine[0][0],currLine[0][1]))
            #     isRight = False

            # if currType == 'A':
            #     p1 = thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine))
            #     p2 = thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine))
            #     p3 = DivSegmInRatio(2 / 1, *currLine)
            #     p4 = DivSegmInRatio(1 / 2, *currLine)
            #     p5 = thirdApex(DivSegmInRatio(1 / 2, *currLine), currLine[0])
            #     p6 = thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine))
            #     p7 = thirdApex(currLine[1], p3)
            #     p8 = currLine[1]
            #
            #     newConv.append((p1, p2))
            #     newConv.append((p2, p3))
            #     newConv.append((p3, p4))
            #     newConv.append((p4, p5))
            #     newConv.append((p5, p6))
            #     newConv.append((p6, p7))
            #     newConv.append((p7, p8))
            #     newRule = 'ABBAAAB'
            #     if isRight:
            #         newOrnt = 'RRLLRRR'
            #     else:
            #         newOrnt = 'LLRRLLL'
            # elif currType == 'B':
            #     p1 = currLine[0]
            #     p2 = thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine))
            #     p3 = thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine))
            #     p4 = thirdApex(DivSegmInRatio(2 / 1, *currLine), currLine[1])
            #     p5 = DivSegmInRatio(2 / 1, *currLine)
            #     p6 = DivSegmInRatio(1 / 2, *currLine)
            #     p7 = thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine))
            #     p8 = thirdApex(currLine[1], DivSegmInRatio(2 / 1, *currLine))
            #
            #     newConv.append((p1, p2))
            #     newConv.append((p2, p3))
            #     newConv.append((p3, p4))
            #     newConv.append((p4, p5))
            #     newConv.append((p5, p6))
            #     newConv.append((p6, p7))
            #     newConv.append((p7, p8))
            #
            #     newRule = 'ABBBAAB'
            #     if isRight:
            #         newOrnt = 'RRRLLRR'
            #     else:
            #         newOrnt = 'LLLRRLL'

            for i in range(len(newConv)):
                finalConv.append(newConv[i])
            finalRule += newRule
            finalOrent += newOrnt

        return gosperOnce(finalConv, finalRule, finalOrent, order-1)
'''
# ТИП B - ЭТО ДВАЖДЫЕ ОТРАЖЁННЫЙ ТИП А
def gosperOnce(arrLines, arrType, order, rotAngle):
    if order == 0:
        return arrLines
    else:
        finalConv = []
        finalRule = ''
        # массив прямых, каждая из которых задаётся 2 точками,
        # каждая из которых задаётся 2 координатами
        # ТИП B - ЭТО ДВАЖДЫЕ ОТРАЖЁННЫЙ ТИП А
        for (currLine, currType) in zip(arrLines, arrType):
            newConv = []
            newRule = ''
            pp = []
            # p1 = thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine))
            # p2 = thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine))
            # p3 = DivSegmInRatio(2 / 1, *currLine)
            # p4 = DivSegmInRatio(1 / 2, *currLine)
            # p5 = thirdApex(DivSegmInRatio(1 / 2, *currLine), currLine[0])
            # p6 = thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine))
            # p7 = thirdApex(currLine[1], p3)
            # p8 = currLine[1]
            # pp.append(p1)
            # pp.append(p2)
            # pp.append(p3)
            # pp.append(p4)
            # pp.append(p5)
            # pp.append(p6)
            # pp.append(p7)
            # pp.append(p8)

            if currType == 'A':
                pp.append(thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine)))
                pp.append(DivSegmInRatio(2 / 1, *currLine))
                pp.append(DivSegmInRatio(1 / 2, *currLine))
                pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), currLine[0]))
                pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(currLine[1], DivSegmInRatio(2 / 1, *currLine)))
                pp.append(currLine[1])

                # поворот:
                for i in range(len(pp)):
                    pp[i] = rotateDot(pp[i], rotAngle)

                for i in range(1, len(pp)):
                    newConv.append((pp[i-1], pp[i]))
                newRule = 'ABBBAAB'
            elif currType == 'B':
                pp.append(currLine[0])
                pp.append(thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine)))
                pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), currLine[1]))
                pp.append(DivSegmInRatio(2 / 1, *currLine))
                pp.append(DivSegmInRatio(1 / 2, *currLine))
                pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(currLine[1], DivSegmInRatio(2 / 1, *currLine)))

                # поворот:
                for i in range(len(pp)):
                    pp[i] = rotateDot(pp[i], rotAngle)

                # pp.append(currLine[1])
                # pp.append(thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine)))
                # pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine)))
                # pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), currLine[1]))
                # pp.append(DivSegmInRatio(2 / 1, *currLine))
                # pp.append(DivSegmInRatio(1 / 2, *currLine))
                # pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine)))
                # pp.append(thirdApex(currLine[1], DivSegmInRatio(2 / 1, *currLine)))

                # pp_temp = ReverseLines(pp)
                # for i in range(1, len(pp_temp)):
                #     newConv.append((pp_temp[i-1], pp_temp[i]))
                for i in range(1, len(pp)):
                    newConv.append((pp[i-1], pp[i]))
                newRule = 'ABBBAAB'

            for i in range(len(newConv)):
                finalConv.append(newConv[i])
            finalRule += newRule

        return gosperOnce(finalConv, finalRule, order-1, rotAngle)

def getRule(iterations):
    axiom, tempAx, logic = 'A', '', {'A': 'A-B--B+A++AA+B-', 'B': '+A-BB--B-A++A+B'}

    for i in range(iterations):
        for j in axiom:
            tempAx += logic[j] if j in logic else j
        axiom, tempAx = tempAx, ''

    return axiom

if __name__ == '__main__':
    step = 6
    phi = getRotateAngle()
    # test = gosperOnce([((0, 0), (step, 0))], 'A', 'R', 1)

    # newL = []
    # order = 2
    # for _ in range(order):
    #     for v in l2:
    #         newL.append(transform_vector(v, np.pi/3, step/3))                # 1
    #         newL.append(transform_vector(v, phi/2, step/3*np.sqrt(3) ))    # 2
    #         newL.append(transform_vector(v, 0, step*2/3))                # 3
    #         newL.append(transform_vector(v, 0, step/3))                # 4
    #         newL.append(transform_vector(v, -phi, step/3))                    # 5
    #         newL.append(transform_vector(v, -phi/2, step/3*np.sqrt(3) ))       # 6
    #         newL.append(transform_vector(v, -phi2, step/3*np.sqrt(7) ))     # 7
    #         newL.append(transform_vector(v, 0, step))       # 8
    #         '''sqrt(3) и sqrt(7) тк диагональ через стороны и угол в парал.'''
    #     l2 = newL.copy()
    #     newL.clear()

    # for i in range(len(l2)):
    #     newL.append([l2[i][0] / 6, np.sqrt(3) / 2 * 1 / 3 * step])
    #     newL.append([l2[i][0] / 2, np.sqrt(3) / 2 * 1 / 3 * step])
    #     newL.append([l2[i][0] * 2 / 3, l2[i][1]])
    #     newL.append([l2[i][0] / 3, l2[i][1]])
    #     newL.append([l2[i][0] / 6, -np.sqrt(3) / 2 * 1 / 3 * step])
    #     newL.append([l2[i][0] / 2, -np.sqrt(3) / 2 * 1 / 3 * step])
    #     newL.append([l2[i][0] * 5 / 6, -np.sqrt(3) / 2 * 1 / 3 * step])
    #     newL.append([l2[i][0], l2[i][1]])
    # l2 = newL
    # # newL += newL

    # поворот отн. своего начала
    # for ch in s:
    #     if ch == 'A' or ch == 'B':
    #         l2.append(
    #             np.round(
    #                     np.array([step, step]) + # [l2[len(l2) - 2][0]
    #                     matCurrAngle @ np.array(np.array(l2[len(l2) - 1]))
    #             , 2)
    #         )
    #         matCurrAngle = np.array([[1, 0],
    #                                  [0, 1]])
    #     elif ch == '+':
    #         matCurrAngle = np.dot(matRotatePlus, matCurrAngle)
    #
    #     elif ch == '-':
    #         matCurrAngle = np.dot(matRotateMinus, matCurrAngle)

    # print(s)
    # print(*l2)
    # x = tuple((zip(m[0], m[1])) for m in l0)

    # plt.plot(x, y, color='green', marker='o', markersize=3)

    # ax = plt.gca()
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')

    l0 = gosperOnce([((0, 0), (step, 0))], 'A', 0, phi)
    # x, y = [], []
    # for dot in l0:
    #     x.append(dot[0][0])
    #     x.append(dot[1][0])
    #     y.append(dot[0][1])
    #     y.append(dot[1][1])
    # ax.plot(x, y, linewidth=8, color='green')

    l1 = gosperOnce([((0, 0), (step, 0))], 'A', 1, phi)
    # x, y = [], []
    # for dot in l1:
    #     x.append(dot[0][0])
    #     x.append(dot[1][0])
    #     y.append(dot[0][1])
    #     y.append(dot[1][1])
    # ax.plot(x, y, linewidth=5, color='black')
    #
    # test_l2_1 = gosperOnce([((1.0, 1.7320508075688772), (3.0, 1.7320508075688772))], 'A', 1)

    def flatten(l):
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from flatten(el)
            else:
                yield el

    l2 = gosperOnce([((0, 0), (step, 0))], 'A', 2, phi)

    lst = [([0.37796447, 1.96396101], [2.26778684, 2.61861468]), ([2.26778684, 2.61861468], [3.77964473, 1.30930734]),
           ([3.77964473, 1.30930734], [1.88982237, 0.65465367]), ([1.88982237, 0.65465367], [1.51185789, -1.30930734]),
           ([1.51185789, -1.30930734], [3.40168026, -0.65465367]),
           ([3.40168026, -0.65465367], [5.29150262e+00, 8.88678020e-13]),
           ([5.29150262e+00, 8.88678020e-13], [5.6694671, 1.96396101])]
    test_l = list(flatten(l2))
    test_l2 = flatten(lst)
    x, y = [], []
    for dot in l2:
        x.append(dot[0][0])
        x.append(dot[1][0])
        y.append(dot[0][1])
        y.append(dot[1][1])
    ax.plot(x, y, linewidth=2, color='r')
    ax.plot(x, y, 'bo')

    # tttt = 1
    # for (xi, yi) in zip(x, y):
    #     plt.text(xi + rd.randint(-1, 1) * (1 / step) * 1.2,
    #              yi,
    #              (tttt), va='bottom', ha='center', size='xx-large')
    #     if (tttt) % 2:
    #         pass
    #     tttt += 1

    plt.show()

    # axiom, tempAx, logic, iterations = 'A', '', {'A': 'A-B--B+A++AA+B-', 'B': '+A-BB--B-A++A+B'}, 1
    #
    # for i in range(iterations):
    #     for j in axiom:
    #         tempAx += logic[j] if j in logic else j
    #     axiom, tempAx = tempAx, ''

    # turtle.left(90)
    # turtle.up()
    # turtle.goto(0, -100)
    # turtle.down()
    # for _ in range(50):
    #     turtle.forward(step)
    #     turtle.dot(5)
    # turtle.up()
    # turtle.goto(-100, 0)
    # turtle.down()
    # turtle.right(90)
    # for _ in range(50):
    #     turtle.forward(step)
    #     turtle.dot(5)
    # turtle.up()
    # turtle.goto(0, 0)
    # turtle.down()
    #

    # turtle.hideturtle()
    turtle.tracer()
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(0, 0)  # 180 240
    turtle.pendown()
    turtle.width(2)

    # s = 'A'
    # s = 'A-B--B+A++AA+B-'
    # s = '+A-BB--B-A++A+B'
    s = getRule(1)

    phi = np.pi / 3
    tPs = []
    cntr = 0
    for k in s:
        cntr += 1
        if k == '+':
            turtle.left(round(np.degrees(phi)))
        elif k == '-':
            turtle.right(round(np.degrees(phi)))
        else:
            turtle.forward(step * 10)

        if cntr % 15 == 0:
            # turtle.dot(size=10)
            pass

        tPs.append(((round(turtle.pos()[0] / 10, 2), round(turtle.pos()[1] / 10, 2))))

    print(*tPs)
    turtle.update()
    turtle.mainloop()

