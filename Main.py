from calendar import calendar
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

# Definindo classes


class Definir_frames(object):
    def __init__(self, master, nome):

        frame = ttk.Frame(master)
        frame.pack(fill='both', expand=1)
        frames_m.add(frame, text=nome)


class Label_frame_class:
    def __init__(self, master, relwidth, relheight, relx, rely):

        self.label_frame = LabelFrame(master)
        self.label_frame.place(relwidth=relwidth,
                          relheight=relheight, relx=relx, rely=rely)


class Label_class:
    def __init__(self, master, texto):

        label = LabelFrame(master, text=texto)
        label.pack(fill='both', expand=1)


class Entry_class:
    def __init__(self, master, relwidth, relheight, relx, rely):

        input = Entry(master)
        input.place(relwidth=relwidth, relheight=relheight,
                    relx=relx, rely=rely)
        lista_entries.append(input)


class Button_class:
    def __init__(self, master, texto, função, relwidth, relheight, relx, rely):

        button = Button(master, text=texto, command=função)
        button.place(relwidth=relwidth, relheight=relheight,
                     relx=relx, rely=rely)


class DateEntry_class:
    def __init__(self, master, relwidth, relheight, relx, rely):
        pass


class Funcoes:
    def pegar():
        for entry in lista_entries:
            data = entry.get()


lista_entries = []
app = Tk()

frames_m = ttk.Notebook(app)
frames_m.pack(fill='both', expand=1)
frame_1 = ttk.Frame(frames_m)
frame_1.pack(fill='both', expand=1)
frames_m.add(frame_1, text='ola')
#frame_1 = Definir_frames(frames_m, 'Romaneios')
lf_1 = Label_frame_class(frame_1, 1, 1, 10, 10)
inp_1 = Entry_class(lf_1, 1, 0.5, 1, 1)

app.mainloop()
