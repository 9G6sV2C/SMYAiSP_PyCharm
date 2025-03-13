import tkinter as tk
import tkinter.messagebox as mb

def EntCounter():
    result = 0
    if entSurname.get() != '': result += 1
    if entName.get() != '': result += 1
    if entPatronymic.get() != '': result += 1
    return result

def RadBtnCounter():
    result = 0
    if groupChoice.get() == gr1: result += 1
    if groupChoice.get() == gr2: result += 1
    if groupChoice.get() == gr3: result += 1
    return result

def ChkBtnCounter():
    result = 0
    if favSubj1_status.get() == 1: result += 1
    if favSubj2_status.get() == 1: result += 1
    if favSubj3_status.get() == 1: result += 1
    if favSubj4_status.get() == 1: result += 1
    if favSubj5_status.get() == 1: result += 1
    return result

def Submit():
    entSurname['state'] = 'disabled'
    entName['state'] = 'disabled'
    entPatronymic['state'] = 'disabled'
    rdbGroup1['state'] = 'disabled'
    rdbGroup2['state'] = 'disabled'
    rdbGroup3['state'] = 'disabled'
    ckbFavSubj1['state'] = 'disabled'
    ckbFavSubj2['state'] = 'disabled'
    ckbFavSubj3['state'] = 'disabled'
    ckbFavSubj4['state'] = 'disabled'
    ckbFavSubj5['state'] = 'disabled'

    msg = f'Заполнено полей: {EntCounter()}' + '\n'
    msg += f'Выбрано радиокнопок: {RadBtnCounter()}' + '\n'
    msg += f'Выбрано флагов: {ChkBtnCounter()}'
    mb.showinfo("Информация", msg)
    root.destroy()


root = tk.Tk()
#root.config(bg="#26242f") или через []

frm1 = tk.Frame(root, borderwidth=1, relief=tk.SOLID, padx=8, pady=10)
entCount = 0
lblSurname = tk.Label(frm1, text='Фамилия:')
entSurname = tk.Entry(frm1)
lblName = tk.Label(frm1, text='Имя:')
entName = tk.Entry(frm1)
lblPatronymic = tk.Label(frm1, text='Отчество:')
entPatronymic = tk.Entry(frm1)
frm1.pack(padx=10, pady=10)
lblSurname.pack()
entSurname.pack()
lblName.pack()
entName.pack()
lblPatronymic.pack()
entPatronymic.pack()

frm2 = tk.Frame(root, borderwidth=1, relief=tk.SOLID, padx=8, pady=10)
rdbCount = 0
gr1 = '4245-020303D'
gr2 = '4247-000000D'
gr3 = '4243-111111D'
groupChoice = tk.IntVar()
lblGroup = tk.Label(frm2, text='Группа:')
rdbGroup1 = tk.Radiobutton(frm2, text=gr1, value=gr1, variable=groupChoice)
rdbGroup2 = tk.Radiobutton(frm2, text=gr2, value=gr2, variable=groupChoice)
rdbGroup3 = tk.Radiobutton(frm2, text=gr3, value=gr3, variable=groupChoice)
frm2.pack(padx=10, pady=10)
lblGroup.pack()
rdbGroup1.pack()
rdbGroup2.pack()
rdbGroup3.pack()

frm3 = tk.Frame(root, borderwidth=1, relief=tk.SOLID, padx=8, pady=10)
ckbBtnCount = 0
lblFavSubj = tk.Label(frm3, text='Любимые предметы:')
favSubj1_status = tk.IntVar()
ckbFavSubj1 = tk.Checkbutton(frm3, text="1", variable=favSubj1_status)
favSubj2_status = tk.IntVar()
ckbFavSubj2 = tk.Checkbutton(frm3, text="2", variable=favSubj2_status)
favSubj3_status = tk.IntVar()
ckbFavSubj3 = tk.Checkbutton(frm3, text="3", variable=favSubj3_status)
favSubj4_status = tk.IntVar()
ckbFavSubj4 = tk.Checkbutton(frm3, text="4", variable=favSubj4_status)
favSubj5_status = tk.IntVar()
ckbFavSubj5 = tk.Checkbutton(frm3, text="5", variable=favSubj5_status)
lblFavSubj.pack()
ckbFavSubj1.pack()
ckbFavSubj2.pack()
ckbFavSubj3.pack()
ckbFavSubj4.pack()
ckbFavSubj5.pack()
frm3.pack(padx=10, pady=10)

frm4 = tk.Frame(root, borderwidth=0, relief=tk.SOLID, padx=8, pady=16)
btnSubmit = tk.Button(frm4, text='Отправить', command=Submit)
frm4.pack()
btnSubmit.pack()

#lblEmpty.pack()

root.mainloop()
