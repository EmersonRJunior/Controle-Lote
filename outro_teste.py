from tkinter import *
from tkinter import ttk

app = Tk()

# lista que ficam salvos os inputs

# Criar widgets de input e salvar os inputs em uma lista

entries = []


class Teste:
    def __init__(self, master):
        self.master = master
        input = Entry(app)
        input.pack()
        entries.append(input)


# função que itera pela lista e insere os inputs no listbox
def pegar():
    for entry in entries:
        data = entry.get()
        lb.insert(0, data)


# Loop atraves da classe para chamar inputs
for i in range(10):
    chamar = Teste(app)

# Listbox
lb = Listbox(app)
lb.pack(side='bottom', expand=1)

# Botão que usa a função 'pegar' para salvar os inputs
bt = Button(app, text='pressione', command=pegar)
bt.pack(side='bottom')
app.mainloop()
