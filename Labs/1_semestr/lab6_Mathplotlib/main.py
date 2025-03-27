import tkinter as tk
from tkinter import ttk
import numpy as np
from tkinter.colorchooser import askcolor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def f1_input(x, a, b, c):
    res = np.array([])
    for el in x:
        temp = np.sin(b * el + c)
        if temp == 0:
            res = np.append(res, 0)
            # raise ZeroDivisionError
        else:
            res = np.append(res, a/temp)
    return res

# Дельтоида
def f2_input(t): return np.array([2*np.cos(t)+np.cos(2*t),
                                  2*np.sin(t)-np.sin(2*t)])

def f1Draw():
    global canvas, GraphColor, graphStyle_var
    global markerStyle_var, graphScale_var, approximation_var

    x = np.linspace(leftX_var.get(), rightX_var.get(), approximation_var.get())
    y = f1_input(x, a_var.get(), b_var.get(), c_var.get())
    x *= graphScale_var.get()
    y *= graphScale_var.get()

    ax.plot(x, y,
            markerStyle_var.get(), linestyle=graphStyle_var.get(), color=GraphColor)

    canvas.draw()
    
def f2Draw():
    global canvas, GraphColor, graphStyle_var
    global markerStyle_var, graphScale_var, approximation_var
    # t = np.linspace(0, 2 * np.pi, 1000)
    t = np.linspace(leftX_var.get(), rightX_var.get(), approximation_var.get())
    x_y = f2_input(t)
    x_y[0] *= graphScale_var.get()
    x_y[1] *= graphScale_var.get()

    ax.plot(x_y[0], x_y[1],
            markerStyle_var.get(), linestyle=graphStyle_var.get(), color=GraphColor)

    canvas.draw()

def CnvsClear():
    global figure, ax
    ax.cla()

def SetBGColor(event): ax.patch.set_facecolor(askcolor()[1])

def SetGraphColor(event):
    global GraphColor
    GraphColor = askcolor()[1]

def check_x(*args):
    if leftX_var.get() <= rightX_var.get():
        errmsg_x_var.set('')
    else:
        errmsg_x_var.set('Неверные границы x.')

def check_t(*args):
    if 0 <= leftT_var.get() <= rightT_var.get() <= 2*np.pi:
        tErrmsg_var.set('')
    else:
        tErrmsg_var.set('Неверные границы t.')

def ImportData():
    global BGColor, GraphColor
    with open('impAndExp_data.txt', 'r') as impFile:
        # Жалко удалять
        # print(graphStyle_var.get(), markerStyle_var.get(), BGColor, GraphColor,
        #       graphScale_var.get(), approximation_var.get(), a_var.get(), b_var.get(),
        #       c_var.get(), leftX_var.get(), rightX_var.get(), leftT_var.get(), rightT_var.get())

        # 1) Стиль графика
        temp_var = impFile.readline()[:-1]
        graphStyle_var.set(temp_var)

        # 2) Стиль маркеров
        temp_var = impFile.readline()[:-1]
        markerStyle_var.set(temp_var)

        # 3) Цвет фона
        temp_var = impFile.readline()[:-1]
        BGColor = temp_var

        # 4) Цвет графика
        temp_var = impFile.readline()[:-1]
        GraphColor = temp_var

        # 5) Масштаб
        temp_var = impFile.readline()[:-1]
        graphScale_var.set(float(temp_var))

        # 6) Степень аппроксимации
        temp_var = impFile.readline()[:-1]
        approximation_var.set(int(temp_var))

        # 7) Значение a
        temp_var = impFile.readline()[:-1]
        a_var.set(int(temp_var))

        # 8) Значение b
        temp_var = impFile.readline()[:-1]
        b_var.set(int(temp_var))

        # 8) Значение c
        temp_var = impFile.readline()[:-1]
        c_var.set(int(temp_var))

        # 10) Значение левой границы x
        temp_var = impFile.readline()[:-1]
        leftX_var.set(int(temp_var))

        # 11) Значение правой границы x
        temp_var = impFile.readline()[:-1]
        rightX_var.set(int(temp_var))

        # 12) Значение левой границы t
        temp_var = impFile.readline()[:-1]
        leftT_var.set(float(temp_var))

        # 13) Значение правой границы t
        temp_var = impFile.readline()[:-1]
        rightT_var.set(float(temp_var))

        # ещё графики но пофиг, устал

        impFile.close()

def ExportData():
    with open('impAndExp_data.txt', 'w') as expFile:
        # 1) Стиль графика
        expFile.write(graphStyle_var.get())
        expFile.write('\n')
        # 2) Стиль маркеров
        expFile.write(markerStyle_var.get())
        expFile.write('\n')
        # 3) Цвет фона
        expFile.write(BGColor)
        expFile.write('\n')
        # 4) Цвет графика
        expFile.write(GraphColor)
        expFile.write('\n')
        # 5) Масштаб
        expFile.write(str(graphScale_var.get()))
        expFile.write('\n')
        # 6) Степень аппроксимации
        expFile.write(str(approximation_var.get()))
        expFile.write('\n')
        # 7) Значение a
        expFile.write(str(a_var.get()))
        expFile.write('\n')
        # 8) Значение b
        expFile.write(str(b_var.get()))
        expFile.write('\n')
        # 8) Значение c
        expFile.write(str(c_var.get()))
        expFile.write('\n')
        # 10) Значение левой границы x
        expFile.write(str(leftX_var.get()))
        expFile.write('\n')
        # 11) Значение правой границы x
        expFile.write(str(rightX_var.get()))
        expFile.write('\n')
        # 12) Значение левой границы t
        expFile.write(str(leftT_var.get()))
        expFile.write('\n')
        # 13) Значение правой границы t
        expFile.write(str(rightT_var.get()))
        expFile.write('\n')

        # ещё графики но пофиг, устал

        expFile.close()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x500")
    frmSttngs = tk.Frame(root)
    frmCanvas = tk.Frame(root)
    plt.axis('equal')

    figure, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(figure, master=frmCanvas)
    toolbar = NavigationToolbar2Tk(canvas, frmCanvas)
    toolbar.update()

    btnImport = tk.Button(frmSttngs, text='⤓', width=4, command=ImportData)
    btnExport = tk.Button(frmSttngs, text='⤒', width=4, command=ExportData)

    graphStyles = ['-', '--', '-.']
    graphStyle_var = tk.StringVar(value=graphStyles[0])
    cmbGraphStyle = ttk.Combobox(frmSttngs, textvariable=graphStyle_var,
                                 values=graphStyles, state='readonly', width=6)

    markerStyles = ['', 'o', 'x']
    markerStyle_var = tk.StringVar(value=markerStyles[0])
    cmbMarkerStyle = ttk.Combobox(frmSttngs, textvariable=markerStyle_var,
                                  values=markerStyles, state='readonly', width=6)

    BGColor = '#ffffff'
    GraphColor = '#000'
    btnBGColor = tk.Button(frmSttngs, text='Цвет фона')
    btnBGColor.bind('<Button-1>', SetBGColor)
    btnGraphColor = tk.Button(frmSttngs, text='Цвет графика')
    btnGraphColor.bind('<Button-1>', SetGraphColor)

    graphScale_var = tk.DoubleVar(root, value=1)
    sclGraphScale = tk.Scale(
        frmSttngs, label='Выберете масштаб:', orient=tk.HORIZONTAL, length=150,
        from_=0.5, to=4, tickinterval=1, resolution=0.1, variable=graphScale_var, width=12)

    approximation_var = tk.IntVar(root, value=100)
    sclApproximation = tk.Scale(
        frmSttngs, label='Аппроксимация:', orient=tk.HORIZONTAL, length=150,
        from_=10, to=1000, tickinterval=270, resolution=45, variable=approximation_var, width=12)

    a_var = tk.IntVar(root, value=1)
    b_var = tk.IntVar(root, value=2)
    c_var = tk.IntVar(root, value=3)
    leftX_var = tk.IntVar(root, value=-2)
    rightX_var = tk.IntVar(root, value=2)
    errmsg_x_var = tk.StringVar(root)
    errmsg_xArgs_var = tk.StringVar(root)
    leftX_var.trace_add(mode='write', callback=check_x)
    rightX_var.trace_add(mode='write', callback=check_x)
    # a_var.trace_add('write', isCorrXArgs)
    # b_var.trace_add('write', isCorrXArgs)
    # c_var.trace_add('write', isCorrXArgs)
    # frmXVariables = tk.Frame(frmSttngs)
    lblA = tk.Label(frmSttngs, text='a = ')
    lblC = tk.Label(frmSttngs, text='c = ')
    lblB = tk.Label(frmSttngs, text='b = ')
    lblX = tk.Label(frmSttngs, text='≤ x ≤')
    lblXErrmsg = tk.Label(frmSttngs, foreground='red', textvariable=errmsg_x_var)
    lblXArgsErrmsg = tk.Label(frmSttngs, foreground='red', textvariable=errmsg_xArgs_var)
    entA = tk.Entry(frmSttngs, width=4, textvariable=a_var)
    entB = tk.Entry(frmSttngs, width=4, textvariable=b_var)
    entC = tk.Entry(frmSttngs, width=4, textvariable=c_var)
    entLeftX = tk.Entry(frmSttngs, width=4, textvariable=leftX_var)
    entRightX = tk.Entry(frmSttngs, width=4, textvariable=rightX_var)

    leftT_var = tk.DoubleVar(root, value=-2*np.pi)
    rightT_var = tk.DoubleVar(root, value=2*np.pi)
    tErrmsg_var = tk.StringVar(root)
    leftT_var.trace_add(mode='write', callback=check_t)
    rightT_var.trace_add(mode='write', callback=check_t)
    lblT = tk.Label(frmSttngs, text='≤ t ≤')
    lblTErrmsg = tk.Label(frmSttngs, foreground='red', textvariable=tErrmsg_var)
    entLeftT = tk.Entry(frmSttngs, width=4, textvariable=leftT_var)
    entRightT = tk.Entry(frmSttngs, width=4, textvariable=rightT_var)

    btnDrawF1 = tk.Button(frmSttngs, text='f1', command=f1Draw)
    btnDrawF2 = tk.Button(frmSttngs, text='f2', command=f2Draw)
    btnClearCnvs = tk.Button(frmSttngs, text='Clear', command=CnvsClear)

    lblF1_1 = tk.Label(frmSttngs, text='f1 = ')
    lblF1_2 = tk.Label(frmSttngs, text='a/sin(b*x+c)')
    lblF2_1 = tk.Label(frmSttngs, text='f2 = ')
    lblF2_2 = tk.Label(frmSttngs, text='x = 2cos(t)+cos(2t),\ny = 2sin(t)−sin(2t),\nt∈[0, 2π]')

    # root.geometry('300x250')
    # root.rowconfigure(index=0, weight=1)
    # root.rowconfigure(index=1, weight=2)

#region Расположение

    frmSttngs.pack(side=tk.LEFT, fill=tk.Y)
    frmCanvas.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.get_tk_widget().pack()

    btnImport.grid(row=0, column=0)
    btnExport.grid(row=0, column=2)

    cmbGraphStyle.grid(row=1, column=0, columnspan=3)
    cmbMarkerStyle.grid(row=2, column=0, columnspan=3)

    btnBGColor.grid(row=3, column=1)
    btnGraphColor.grid(row=4, column=1)

    sclGraphScale.grid(row=5, column=0, columnspan=3)
    sclApproximation.grid(row=6, column=0, columnspan=3)

    # frmXVariables.grid(row=6, column=0)
    lblA.grid(row=7, column=0)
    entA.grid(row=7, column=1)
    lblB.grid(row=8, column=0)
    entB.grid(row=8, column=1)
    lblC.grid(row=9, column=0)
    entC.grid(row=9, column=1)
    entLeftX.grid(row=10, column=0)
    lblX.grid(row=10, column=1)
    entRightX.grid(row=10, column=2)
    lblXErrmsg.grid(row=11, column=0, columnspan=3)

    # frmTVariables.grid(row=6, column=2)
    entLeftT.grid(row=12, column=0)
    lblT.grid(row=12, column=1)
    entRightT.grid(row=12, column=2)
    lblTErrmsg.grid(row=13, column=0, columnspan=3)

    btnDrawF1.grid(row=14, column=0)
    btnClearCnvs.grid(row=14, column=1)
    btnDrawF2.grid(row=14, column=2)

    lblF1_1.grid(row=15, column=0)
    lblF1_2.grid(row=15, column=1)
    lblF2_1.grid(row=16, column=0)
    lblF2_2.grid(row=16, column=1)





    # lblFuncs.grid(row=0, column=0, columnspan=4)
    # rdbFunc1.grid(row=1, column=0)
    # rdbFunc2.grid(row=1, column=2)
    # sclGraphScale.grid(row=2, column=0, columnspan=4)
    #
    # btnBGColor.grid(row=4, column=0, columnspan=4)

# endregion

    tk.mainloop()