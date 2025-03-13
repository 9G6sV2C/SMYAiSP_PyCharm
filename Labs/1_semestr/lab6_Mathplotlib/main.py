# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import ttk
import numpy as np
from tkinter.colorchooser import askcolor
import matplotlib.pyplot as plt
from fontTools.misc.cython import returns
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def f1_input(x, a, b, c):
    return a/np.sin(b*x+c)
    # while True:
    #     try:
    #         if np.sin(b*x+c).all() == 0:
    #             raise ZeroDivisionError('np.sin(b*x+c) = 0')
    #     except ZeroDivisionError:
    #         print('Деление на ноль.')
    #     else:
    #         return a/np.sin(b*x+c)

qwe = f1_input(np.array([1]), 1, 0, 0)
print(qwe)
print(qwe[0] == np.inf)

# Дельтоида
def f2_input(t): return (2*np.cos(t)+np.cos(2*t), 2*np.sin(t)-np.sin(2*t))
    # while True:
    #     try:
    #         if 0 <= t <= 2*np.pi:
    #             raise ArithmeticError('t должно быть 0 <= t <= 2*.pi!')
    #     except ZeroDivisionError:
    #         print('хз пока.')
    #     else:
    #         return (2*np.cos(t)+np.cos(2*t), 2*np.sin(t)-np.sin(2*t))

def f1Draw():
    # the figure that will contain the plot
    fig = plt.Figure(figsize=(5, 5), dpi=100)

    x = np.linspace(leftX_var.get(), rightX_var.get(), 100)
    y = f1_input(x, a_var.get(), b_var.get(), c_var.get())

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(x, y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frmCanvas)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, frmCanvas)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def f2Draw():
    # the figure that will contain the plot
    fig = plt.Figure(figsize=(5, 5), dpi=100)

    x = np.linspace(leftT_var.get(), rightT_var.get(), 100)
    y = f2_input(x)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y[0], y[1])

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frmCanvas)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, frmCanvas)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def CnvsClear():
    pass

def SetColor(event):
    global BGColor_var
    RGB, BGColor_var = askcolor()  # запоминаем результат выбора цвета # !!!

def isCorrX(*args):
    if leftX_var.get() <= rightX_var.get():
        xErrmsg_var.set('')
    else:
        xErrmsg_var.set('Неверные границы.')

# def isCorrXArgs(*args):
#     if np.sin(b_var.get()*x+c_var.get()).all() == 0:
#         xErrmsg_var.set('')
#     else:
#         xErrmsg_var.set('Неверные границы.')

def isCorrT(*args):
    if leftT_var.get() <= rightT_var.get():
        tErrmsg_var.set('')
    else:
        tErrmsg_var.set('Неверные границы.')

if __name__ == '__main__':
    root = tk.Tk()
    frmSttngs = tk.Frame(root)
    frmCanvas = tk.Frame(root)

    btnImport = tk.Button(frmSttngs, text='⤓')
    btnExport = tk.Button(frmSttngs, text='⤒')

    graphStyles = ['test1', 'test2', 'test3', 'test4']
    graphStyle_var = tk.StringVar(value=graphStyles[0])
    cmbGraphStyle = ttk.Combobox(frmSttngs, textvariable=graphStyle_var,
                                 values=graphStyles, state='readonly', width=6)

    markerStyles = ['test11', 'test22', 'test33', 'test44']
    markerStyle_var = tk.StringVar(value=markerStyles[0])
    cmbMarkerStyle = ttk.Combobox(frmSttngs, textvariable=markerStyle_var,
                                  values=markerStyles, state='readonly', width=6)

    BGColor_var = '#ffffff'
    GraphColor_var = '#000'
    btnBGColor = tk.Button(frmSttngs, text='Цвет фона')
    btnBGColor.bind('<Button-1>', SetColor)
    btnGraphColor = tk.Button(frmSttngs, text='Цвет графика')
    btnGraphColor.bind('<Button-1>', SetColor)

    # lblGraphScale = tk.Label(frmSttngs, text='Выберете масштаб:')
    GraphScale_var = tk.IntVar()
    GraphScale_var.set(1)
    sclGraphScale = tk.Scale(
        frmSttngs, label='Выберете масштаб:', orient=tk.HORIZONTAL, length=150,
        from_=0.5, to=4, tickinterval=1, resolution=0.1, variable=GraphScale_var, width=12)

    a_var = tk.IntVar(root)
    b_var = tk.IntVar(root)
    c_var = tk.IntVar(root)
    leftX_var = tk.IntVar(root)
    rightX_var = tk.IntVar(root)
    xErrmsg_var = tk.StringVar(root)
    xArgsErrmsg_var = tk.StringVar(root)
    leftX_var.trace_add('write', isCorrX)
    rightX_var.trace_add('write', isCorrX)
    # a_var.trace_add('write', isCorrXArgs)
    # b_var.trace_add('write', isCorrXArgs)
    # c_var.trace_add('write', isCorrXArgs)
    # frmXVariables = tk.Frame(frmSttngs)
    lblA = tk.Label(frmSttngs, text='a = ')
    lblC = tk.Label(frmSttngs, text='c = ')
    lblB = tk.Label(frmSttngs, text='b = ')
    lblX = tk.Label(frmSttngs, text='≤ x ≤')
    lblXErrmsg = tk.Label(frmSttngs, foreground='red', textvariable=xErrmsg_var)
    lblXArgsErrmsg = tk.Label(frmSttngs, foreground='red', textvariable=xArgsErrmsg_var)
    entA = tk.Entry(frmSttngs, width=4, textvariable=a_var)
    entB = tk.Entry(frmSttngs, width=4, textvariable=b_var)
    entC = tk.Entry(frmSttngs, width=4, textvariable=c_var)
    entLeftX = tk.Entry(frmSttngs, width=4, textvariable=leftX_var)
    entRightX = tk.Entry(frmSttngs, width=4, textvariable=rightX_var)

    leftT_var = tk.IntVar()
    rightT_var = tk.IntVar()
    tErrmsg_var = tk.StringVar(root)
    leftT_var.trace_add('write', isCorrT)
    rightT_var.trace_add('write', isCorrT)
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

    frmSttngs.pack(side=tk.LEFT, fill=tk.Y)
    frmCanvas.pack(side=tk.RIGHT, fill=tk.Y)

    btnImport.grid(row=0, column=0)
    btnExport.grid(row=0, column=2)

    cmbGraphStyle.grid(row=1, column=0, columnspan=3)
    cmbMarkerStyle.grid(row=2, column=0, columnspan=3)

    btnBGColor.grid(row=3, column=1)
    btnGraphColor.grid(row=4, column=1)

    sclGraphScale.grid(row=5, column=0, columnspan=3)

    # frmXVariables.grid(row=6, column=0)
    lblA.grid(row=6, column=0)
    entA.grid(row=6, column=1)
    lblB.grid(row=7, column=0)
    entB.grid(row=7, column=1)
    lblC.grid(row=8, column=0)
    entC.grid(row=8, column=1)
    entLeftX.grid(row=9, column=0)
    lblX.grid(row=9, column=1)
    entRightX.grid(row=9, column=2)
    lblXErrmsg.grid(row=10, column=0, columnspan=3)

    # frmTVariables.grid(row=6, column=2)
    entLeftT.grid(row=11, column=0)
    lblT.grid(row=11, column=1)
    entRightT.grid(row=11, column=2)
    lblTErrmsg.grid(row=12, column=0, columnspan=3)

    btnDrawF1.grid(row=13, column=0)
    btnClearCnvs.grid(row=13, column=1)
    btnDrawF2.grid(row=13, column=2)

    lblF1_1.grid(row=14, column=0)
    lblF1_2.grid(row=14, column=1)
    lblF2_1.grid(row=15, column=0)
    lblF2_2.grid(row=15, column=1)





    # lblFuncs.grid(row=0, column=0, columnspan=4)
    # rdbFunc1.grid(row=1, column=0)
    # rdbFunc2.grid(row=1, column=2)
    # sclGraphScale.grid(row=2, column=0, columnspan=4)
    #
    # btnBGColor.grid(row=4, column=0, columnspan=4)
    


    tk.mainloop()