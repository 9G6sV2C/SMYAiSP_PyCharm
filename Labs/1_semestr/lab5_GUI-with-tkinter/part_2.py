import tkinter as tk
import numpy as np
from tkinter.colorchooser import askcolor
from collections.abc import Iterable

def ClrCanvas(event):
    cnvs.delete('all')

def SetColor(event):
    global _color
    RGB, _color = askcolor()  # запоминаем результат выбора цвета # !!!
    
def ChoiceMaxPowerByType():
    if _curveType.get() == 0: # кривая Коха
        sclPower.config(tickinterval=1, to=6)
    elif _curveType.get() == 1: # треугольник Серпинского
        sclPower.config(tickinterval=1, to=7)
    elif _curveType.get() == 2: # кривая дракона
        sclPower.config(tickinterval=4, to=17)
    else: # Кривая Госпера
        sclPower.config(tickinterval=1, to=6)
        
def ChoiceMaxWidthByType():
    if _curveType.get() == 0:  # кривая Коха
        sclPenWidth.config(tickinterval=1, to=10)
    elif _curveType.get() == 1: # треугольник Серпинского
        sclPenWidth.config(tickinterval=1, to=10)
    elif _curveType.get() == 2:  # кривая дракона
        sclPenWidth.config(tickinterval=4, to=17)
    else:  # Кривая Госпера
        sclPenWidth.config(tickinterval=6, to=27)

def Koch(order, x1, y1, x2, y2):
    if order == 0:
        cnvs.create_line(x1,y1,x2,y2,fill=_color, width=_penWidth.get())
    else:
        alpha = np.atan2(y2-y1, x2-x1)
        R = np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
        # вычислим xA, yA, xB, yB, xC, yC
        xA = x1+(R/3)*np.cos(alpha)
        yA = y1+(R/3)*np.sin(alpha)
        xC = xA+R*np.cos(alpha-np.pi/3)/3
        yC = yA+R*np.sin(alpha-np.pi/3)/3
        xB = x1+2*R*np.cos(alpha)/3
        yB = y1+2*R*np.sin(alpha)/3
        #рекурсивные вызовы
        Koch(order-1, x1, y1, xA, yA)
        Koch(order-1, xA, yA, xC, yC)
        Koch(order-1, xC, yC, xB, yB)
        Koch(order-1, xB, yB, x2, y2)
    
def Sierpinski(order, x, y, length):
    s3d2 = np.sqrt(3)/2
    # строим цветной треугольник ABC
    # вычисляем координаты вершин треугольника
    points = [x, y, x+length/2, y-length*s3d2, x+length, y]
    cnvs.create_polygon(points, outline=_color, fill=_color, width = _penWidth.get())
    # теперь будем «выбрасывать» средние треугольники
    if order > 0:
        # рисуем треугольник MNK цветом фона
        points = [x+length/4, y-length*s3d2/2, x+3*length/4, y-length*s3d2/2,
        x+length/2, y]
        cnvs.create_polygon(points, outline='#fff', fill='#fff', width=_penWidth.get())
        #рекурсивно вызываем фунцкию
        Sierpinski(order-1, x, y, length/2) # в т.A
        Sierpinski(order-1, x+length/2, y, length/2) # в т.K
        Sierpinski(order-1, x+length/4, y-length*s3d2/2, length/2) # в т.M

def getDragonPoints(order):
    x = cnvs.winfo_width()/5
    y = cnvs.winfo_height()/2
    if order == 0:
    # ломаная нулевого порядка состоит из одного сегмента
        res = []
        res.append(x)
        res.append(y+x/2)
        res.append(cnvs.winfo_width()-x)
        res.append(y+x/2)
        return res
    prevRes = getDragonPoints(order-1)
    res = []
    # направление: 1 - влево, -1 - вправо
    DirSign = 1
    # начальная точка ломаной не изменяется
    res.append(prevRes[0])
    res.append(prevRes[1])
    for i in range(0, len(prevRes)-3, 2):
        # считаем очередной сегмент ломаной
        p1x = prevRes[i]
        p1y = prevRes[i+1]
        p2x = prevRes[i+2]
        p2y = prevRes[i+3]
        alpha = np.atan2(p2y - p1y, p2x - p1x)-DirSign*np.pi/4
        R = np.sqrt(((p1x - p2x) * (p1x - p2x) +
        (p1y - p2y) * (p1y - p2y))/2)
        # найдем новую точку ломаной
        pcx = p1x+R*np.cos(alpha)
        pcy = p1y+R*np.sin(alpha)
        # добавляем ее и конечную точку в список точек ломаной
        res.append(pcx)
        res.append(pcy)
        res.append(p2x)
        res.append(p2y)
        # меняем направление
        DirSign *= -1
    return res

def Gosper(s, order):
    # с помощью L-систем
    # A,B - вперёд, + - поворот на pi/3 влево, a - поворот на pi/3 вправо
    for _ in range(order):
        if s == 'A':
            s = s.replace('A', 'A-B--B+A++AA+B-')
        else:
            s = s.replace('A', 'A-B--B+A++AA+B-')
            s = s.replace('B', '+A-BB--B-A++A+B')
    return s

def gosperOnce(arrLines, arrType, order, rotAngle):
    
    # ф-я нахождения коорд. 3-ей вершины в правильном треугольнике по 2 другим
    def thirdApex(*points):  # points -> ( (x1, y1), (x2, y2)) )
        xp = points[1][0] - points[0][0]
        yp = points[1][1] - points[0][1]
        x3 = points[0][0] + 0.5 * (xp - yp * np.sqrt(3))
        y3 = points[0][1] + 0.5 * (xp * np.sqrt(3) + yp)
        return (x3, y3)

    # ф-я нахождения коорд. k-ой части отрезка
    def DivSegmInRatio(k, *ps):  # ps -> ( (x1, y1), (x2, y2)) )
        return ((ps[0][0] + k * ps[1][0]) / (1 + k), (ps[0][1] + k * ps[1][1]) / (1 + k))

    # ф-я поворота функции на заданный угол
    def rotateDot(vector, angle):
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])

        rotated_vector = rotation_matrix @ vector

        return rotated_vector

    def getRotateAngle():
        return 0.333473172252  # (в радианах) вычеслен в desmos экперементально
    
    
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

            if currType == 'A':
                pp.append(thirdApex(currLine[0], DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), DivSegmInRatio(2 / 1, *currLine)))
                pp.append(DivSegmInRatio(2 / 1, *currLine))
                pp.append(DivSegmInRatio(1 / 2, *currLine))
                pp.append(thirdApex(DivSegmInRatio(1 / 2, *currLine), currLine[0]))
                pp.append(thirdApex(DivSegmInRatio(2 / 1, *currLine), DivSegmInRatio(1 / 2, *currLine)))
                pp.append(thirdApex(currLine[1], DivSegmInRatio(2 / 1, *currLine)))
                pp.append(currLine[1])

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

                for i in range(len(pp)):
                    pp[i] = rotateDot(pp[i], rotAngle)

                for i in range(1, len(pp)):
                    newConv.append((pp[i-1], pp[i]))
                newRule = 'ABBBAAB'

            for i in range(len(newConv)):
                finalConv.append(newConv[i])
            finalRule += newRule

        return gosperOnce(finalConv, finalRule, order-1, rotAngle)

def drawCurve(event):
    # Универсальное решение для списков с любой глубиной вложенности:
    def flatten(l):
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from flatten(el)
            else:
                yield el

    # пусть перед каждым рисованием будем очищать рисунок
    ClrCanvas(event)
    if _curveType.get() == 0:  # кривая Коха
        x1 = 0
        y1 = cnvs.winfo_height()
        x2 = cnvs.winfo_width()
        y2 = 0
        # рекурсия для Коха
        Koch(_curvePower.get(), x1, y1, x2, y2)
    elif _curveType.get() == 1: # треугольник Серпинского
        Sierpinski(_curvePower.get(),0, cnvs.winfo_height() - 20, cnvs.winfo_width() - 10)
    elif _curveType.get() == 2: # кривая дракона
        points = getDragonPoints(_curvePower.get())
        cnvs.create_line(points, fill=_color, width=_penWidth.get())
    else: # Кривая Госпера
        # rotAngle (в радианах) вычеслен экперементально в desmos
        points_temp = gosperOnce([((0,0),(0,6))], 'A', _curvePower.get(), 0.333473172252)
        points = list(flatten(points_temp))
        for i in range(len(points)):
            points[i] *= 40
            if (i+1) % 2 == 0:
                points[i] += cnvs.winfo_width() / 5
            else:
                points[i] += cnvs.winfo_height() / 2
        cnvs.create_line(points, fill=_color, width=_penWidth.get())

if __name__ == '__main__':
    root = tk.Tk()
    # root.geometry('1280x720')

    frmPicture = tk.Frame(root)
    frmSettings = tk.Frame(root)
    frmPicture.pack(side=tk.LEFT)
    frmSettings.pack(side=tk.RIGHT)

    cnvs = tk.Canvas(frmPicture, width=400, height=400)
    cnvs.create_rectangle(0,0, 400, 400, outline='#fff', fill = '#fff')
    cnvs.pack(fill=tk.BOTH, expand=1)

    frm1 = tk.Frame(frmSettings)
    _curveType = tk.IntVar()
    _curveType.set(0)
    rdb0 = tk.Radiobutton(
        frm1, text="Кривая Коха", variable=_curveType, value=0,
        command=lambda: (ChoiceMaxPowerByType(), ChoiceMaxWidthByType()))
    rdb1 = tk.Radiobutton(
        frm1, text="Салфетка Серпинского", variable=_curveType, value=1,
        command=lambda: (ChoiceMaxPowerByType(), ChoiceMaxWidthByType()))
    rdb2 = tk.Radiobutton(
        frm1, text="Драконова ломаная", variable=_curveType, value=2,
        command=lambda: (ChoiceMaxPowerByType(), ChoiceMaxWidthByType()))
    rdb3 = tk.Radiobutton(
        frm1, text="Кривая Госпера", variable=_curveType, value=3,
        command=lambda: (ChoiceMaxPowerByType(), ChoiceMaxWidthByType()))
    frm1.pack()
    rdb0.pack(side=tk.TOP, anchor=tk.W)
    rdb1.pack(side=tk.TOP, anchor=tk.W)
    rdb2.pack(side=tk.TOP, anchor=tk.W)
    rdb3.pack(side=tk.TOP, anchor=tk.W)

    frm2 = tk.Frame(frmSettings)
    _color = "#000"
    btnColor = tk.Button(frm1, text="Цвет")
    btnColor.bind('<Button-1>', SetColor)
    _penWidth = tk.IntVar()
    _penWidth.set(1) # установим ее равной 1 по умолчанию
    sclPenWidth = tk.Scale(
        frm2, label="Толщина линии", orient=tk.HORIZONTAL, length=150,
        from_=1, to=10, tickinterval=1, resolution=1, variable=_penWidth)
    _curvePower=tk.IntVar()
    _curvePower.set(0)
    sclPower = tk.Scale(
        frm2, label="Порядок кривой", orient=tk.HORIZONTAL, length=150,
        from_=0, to=6, tickinterval=1, resolution=1, variable=_curvePower)
    frm2.pack()
    btnColor.pack()
    sclPenWidth.pack()
    sclPower.pack()

    frm3 = tk.Frame(frmSettings)
    btnDraw = tk.Button(frm3, text="Рисовать", width=12)
    btnDraw.bind("<Button-1>", drawCurve)
    btnClear = tk.Button(frm3, text="Стереть", width=12)
    btnClear.bind("<Button-1>", ClrCanvas)
    frm3.pack()
    btnDraw.pack()
    btnClear.pack()

    tk.mainloop()