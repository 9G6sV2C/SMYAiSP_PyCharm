import tkinter as tk

from PIL.ImageCms import Flags


# from tkinter import messagebox

def StartStop():
    global isRunMotion
    isRunMotion = not isRunMotion
    if isRunMotion:
        startBtn['text'] = "Stop"
    else:
        startBtn['text'] = "Restart"
    
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
        
def ReadData(*arg):
    global isGetData
    isGetData = True
    
def MoveBall_NOTWORK():
    global x, y, vx, vy, isRunMotion, _ballRadius

    while isRunAll:
        cnv.delete(tk.ALL)
        cnv.create_oval(x-_ballRadius.get(), y-_ballRadius.get(),
                        x+_ballRadius.get(), y+_ballRadius.get(), fill=ballColor)
        cnv.update()

        if isRunMotion:
            if (x+_ballRadius.get()) >= WIDTH:
                vx = -abs(vx)
            elif (y+_ballRadius.get()) >= HEIGHT:
                vy = -abs(vy)
            elif x <= _ballRadius.get():
                vx = abs(vx)
            elif y <= _ballRadius.get():
                vy = abs(vy)

            x += vx
            y += vy + 0.5 * _gravity.get()
            vy += _gravity.get()

        # elif isGetData:
        #     # try:
        #     #     _ballRadius.set(float(radiusEnt.get()))
        #     # except ValueError:
        #     #     pass
        #     # try:
        #     #     ay = float(GravityEnt.get())
        #     # except ValueError:
        #     #     pass
        #
        #     radiusEnt.delete(0, 'end')
        #     radiusEnt.insert(0, '{:.2f}'.format(_ballRadius.get()))
        #     GravityEnt.delete(0, 'end')
        #     GravityEnt.insert(0, '{:.2f}'.format(ay))
        #     isGetData = False

        cnv.after(FPS, MoveBall)

def ValidRadius(newValue, errorEnt):
    if newValue == '' or not newValue.isdigit():
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

    root.bind('<Return>', ReadData)

    toolbarFrm = tk.Frame(root)
    toolbarFrm.grid(row=0, column=0, sticky ='n')

    cnv = tk.Canvas(root, width = WIDTH, height = HEIGHT, background = "white")
    cnv.grid(row=1, column = 0)

    cnv.bind('<Button-1>', GrabBall)
    cnv.bind('<B1-Motion>', DragBall)
    cnv.bind('<ButtonRelease-1>', ReleaseBall)

    startBtn = tk.Button(toolbarFrm, text="Start", command = StartStop)
    startBtn.grid(row=0, column=0)
    closeBtn=tk.Button(toolbarFrm, text= "Close", command=StopAll)
    closeBtn.grid(row=0, column=1)

    _ballRadius = tk.IntVar(value=35)
    _gravity = tk.DoubleVar(value=0.1)
    radiusLbl = tk.Label(toolbarFrm, text="Radius:")
    radiusEnt = tk.Entry(toolbarFrm, bd = 5, width = 8, textvariable=_ballRadius)
    GravityLbl = tk.Label(toolbarFrm, text="Gravity:")
    GravityEnt = tk.Entry(toolbarFrm, bd = 5, width = 8, textvariable=_gravity)
    radiusLbl.grid(row=1, column=0)
    radiusEnt.grid(row=1, column=1)
    GravityLbl.grid(row=2, column=0)
    GravityEnt.grid(row=2, column=1)

    ballColor = 'green'
    x = _ballRadius.get()
    y = HEIGHT - _ballRadius.get()
    vx = 4.0    
    vy = -7.5
    ay = _gravity.get()

    while isRunAll:
        cnv.delete(tk.ALL)
        cnv.create_oval(x-_ballRadius.get(), y-_ballRadius.get(),
                        x+_ballRadius.get(), y+_ballRadius.get(), fill=ballColor)
        cnv.update()

        if isRunMotion:
            if (x+_ballRadius.get()) >= WIDTH:
                vx = -abs(vx)
            elif (y+_ballRadius.get()) >= HEIGHT:
                vy = -abs(vy)
            elif x <= _ballRadius.get():
                vx = abs(vx)
            elif y <= _ballRadius.get():
                vy = abs(vy)

            x += vx
            y += vy + 0.5 * _gravity.get()
            vy += _gravity.get()

        # elif isGetData:
        #     # try:
        #     #     _ballRadius.set(float(radiusEnt.get()))
        #     # except ValueError:
        #     #     pass
        #     # try:
        #     #     ay = float(GravityEnt.get())
        #     # except ValueError:
        #     #     pass
        #
        #     radiusEnt.delete(0, 'end')
        #     radiusEnt.insert(0, '{:.2f}'.format(_ballRadius.get()))
        #     GravityEnt.delete(0, 'end')
        #     GravityEnt.insert(0, '{:.2f}'.format(ay))
        #     isGetData = False

        cnv.after(FPS)

    root.destroy()