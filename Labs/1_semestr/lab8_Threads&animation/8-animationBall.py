import tkinter as tk
import numpy as np

from PIL.ImageCms import Flags # для .after()


# from tkinter import messagebox

def StartStop():
    global isRunMotion
    isRunMotion = not isRunMotion
    if isRunMotion:
        startBtn['text'] = "Stop"
    else:
        startBtn['text'] = "Continue"
    
def StopAll():
    global isRunAll
    isRunAll = False

def GrabBall(event):
    global isGrabbed, isRunMotion, x, y, _ballRadius
    if not isRunMotion:
        isGrabbed = ((x - event.x)**2 + (y - event.y)**2) < _ballRadius.get()**2
        
def ReleaseBall(event):
    global isGrabbed
    isGrabbed = False
    
def DragBall(event):
    global isGrabbed, x, y
    if isGrabbed:
        x = event.x
        y = event.y
        
# def ReadData(*arg):
#     global isGetData
#     isGetData = True
    
def MoveBall_NOTWORK():
    global x, y, speed_x, speed_y, isRunMotion, _ballRadius

    while isRunAll:
        cnv.delete(tk.ALL)
        cnv.create_oval(x-_ballRadius.get(), y-_ballRadius.get(),
                        x+_ballRadius.get(), y+_ballRadius.get(), fill=ballColor)
        cnv.update()

        if isRunMotion:
            if (x+_ballRadius.get()) >= WIDTH:
                speed_x = -abs(speed_x)
            elif (y+_ballRadius.get()) >= HEIGHT:
                speed_y = -abs(speed_y)
            elif x <= _ballRadius.get():
                speed_x = abs(speed_x)
            elif y <= _ballRadius.get():
                speed_y = abs(speed_y)

            x += speed_x
            y += speed_y + 0.5 * _gravity.get()
            speed_y += _gravity.get()

        # elif isGetData:
        #     # try:
        #     #     _ballRadius.set(float(radiusEnt.get()))
        #     # except ValueError:
        #     #     pass
        #     # try:
        #     #
        #     # acceleration_y = float(GravityEnt.get())
        #     # except ValueError:
        #     #     pass
        #
        #     radiusEnt.delete(0, 'end')
        #     radiusEnt.insert(0, '{:.2f}'.format(_ballRadius.get()))
        #     GravityEnt.delete(0, 'end')
        #     GravityEnt.insert(0, '{:.2f}'.format(
        #     acceleration_y))
        #     isGetData = False

        cnv.after(FPS, MoveBall)

def ValidInt(newValue):
    if newValue == '' or not newValue.isdigit():
        return False
        # messagebox.showerror('Ошибка', 'Радиус не может быть пустым.')
    return True

def ValidFloat(newValue):
    if newValue == '' or (not newValue.isdigit() or not newValue.find('.')):
        return False
        # messagebox.showerror('Ошибка', 'Радиус не может быть пустым.')
    return True


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Шарик и GUI")

    isRunMotion = False
    isRunAll = True
    isGrabbed = False
    isGetData = False
    WIDTH = 800
    HEIGHT = 640
    FPS = 20

    radiusChecker = (root.register(ValidInt), '%P')
    gravityChecker = (root.register(ValidFloat), '%P')

    toolbarFrm = tk.Frame(root)
    toolbarFrm.grid(row=0, column=0, sticky ='n')

    cnv = tk.Canvas(root, width = WIDTH, height = HEIGHT, background = "white")
    cnv.grid(row=1, column = 0)

    # root.bind('<Return>', ReadData)
    cnv.bind('<Button-1>', GrabBall)
    cnv.bind('<B1-Motion>', DragBall)
    cnv.bind('<ButtonRelease-1>', ReleaseBall)

    startBtn = tk.Button(toolbarFrm, text="Start", command = StartStop)
    startBtn.grid(row=0, column=0)
    closeBtn=tk.Button(toolbarFrm, text= "Close", command=StopAll)
    closeBtn.grid(row=0, column=1)

    _ballRadius = tk.IntVar(value=35)
    _gravity = tk.DoubleVar(value=0.1)
    _gravityTest = tk.StringVar(value='0.1a')
    radiusLbl = tk.Label(toolbarFrm, text="Radius:")
    radiusEnt = tk.Entry(toolbarFrm, bd = 5, width = 8, textvariable=_ballRadius,
                         validate='key', validatecommand=radiusChecker)
    GravityLbl = tk.Label(toolbarFrm, text="Gravity:")
    GravityEnt = tk.Entry(toolbarFrm, bd = 5, width = 8, textvariable=_gravityTest,
                          validate='key', validatecommand=gravityChecker)
    radiusLbl.grid(row=1, column=0)
    radiusEnt.grid(row=1, column=1)
    GravityLbl.grid(row=2, column=0)
    GravityEnt.grid(row=2, column=1)

    applyBtn = tk.Button(toolbarFrm, text='Apply', command=lambda: ())

    ballColor = 'green'
    x = _ballRadius.get()
    y = HEIGHT - _ballRadius.get()
    speed_x = np.random.randint(10)
    speed_y = -7.5

    acceleration_y = _gravity.get()

    while isRunAll:
        cnv.delete(tk.ALL)
        cnv.create_oval(x-_ballRadius.get(), y-_ballRadius.get(),
                        x+_ballRadius.get(), y+_ballRadius.get(), fill=ballColor)
        cnv.update()

        if isRunMotion:
            if (x+_ballRadius.get()) >= WIDTH:
                speed_x = -abs(speed_x)
            elif (y+_ballRadius.get()) >= HEIGHT:
                speed_y = -abs(speed_y)
            elif x <= _ballRadius.get():
                speed_x = abs(speed_x)
            elif y <= _ballRadius.get():
                speed_y = abs(speed_y)

            x += speed_x
            y += speed_y + 0.5 * acceleration_y
            speed_y += acceleration_y

        # elif isGetData:
        #     # try:
        #     #     _ballRadius.set(float(radiusEnt.get()))
        #     # except ValueError:
        #     #     pass
        #     # try:
        #     #
        #     #     acceleration_y = float(GravityEnt.get())
        #     # except ValueError:
        #     #     pass
        #
        #     radiusEnt.delete(0, 'end')
        #     radiusEnt.insert(0, '{:.2f}'.format(_ballRadius.get()))
        #     GravityEnt.delete(0, 'end')
        #     GravityEnt.insert(0, '{:.2f}'.format(
        #     acceleration_y))
        #     isGetData = False

        cnv.after(FPS)

    root.destroy()