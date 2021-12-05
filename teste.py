from tkinter import *
from tkinter import ttk


class Criar_input(object):
    def __init__(self, master):
        self.master = master

        self.input = Entry(master)
        self.input.pack()


def getting():
    frase_1 = input_1.input.get()
    frase_2 = input_2.input.get()
    frase_3 = input_3.input.get()
    frase_4 = input_4.input.get()
    frase_5 = input_5.input.get()
    frase_6 = input_6.input.get()
    frase_7 = input_7.input.get()
    frase_8 = input_8.input.get()
    frase_9 = input_9.input.get()
    frase_10 = input_10.input.get()
    lb.insert(0, frase_1)
    lb.insert(1, frase_2)
    lb.insert(2, frase_3)
    lb.insert(3, frase_4)
    lb.insert(4, frase_5)
    lb.insert(5, frase_6)
    lb.insert(6, frase_7)
    lb.insert(7, frase_8)
    lb.insert(8, frase_9)
    lb.insert(9, frase_10)


def get_input(master):
    bt = Button(master, text='Pressione', command=getting)
    bt.pack(side='bottom', expand=1)


app = Tk()

input_1 = Criar_input(app)
input_2 = Criar_input(app)
input_3 = Criar_input(app)
input_4 = Criar_input(app)
input_5 = Criar_input(app)
input_6 = Criar_input(app)
input_7 = Criar_input(app)
input_8 = Criar_input(app)
input_9 = Criar_input(app)
input_10 = Criar_input(app)

lb = Listbox(app)
lb.pack(side='bottom', expand=1)
get_input(app)

app.mainloop()
