# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
root = Tk()


def ff():
    print(leftX_var.get())
    print('->',root.getvar(name='leftX_var'))
    print(type(root.getvar(name='leftX_var')))

leftX_var = IntVar(root, name='leftX_var')
leftX_var.set(123)

ff()

# Tkinter variables
# Giving user defined names to each variables
# so that variables can be modified easily
intvar = IntVar(root, name ="int")
leftX_var = IntVar(root, name='leftX_var')

# Setting values of variables
# using setvar() method
root.setvar(name ="int", value = 100)
root.setvar(name='leftX_var', value=666)

# getting values of each variables using getvar() method
print(root.getvar(name ="int"))
print(root.getvar(name ="leftX_var"))
