from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

app = Tk()
app.geometry('300x500')


class Pagina_1:
    lf_p = LabelFrame(app)
    lf_p.place(relwidth=1, relheight=1)
    lf_top = LabelFrame(lf_p, text='top')
    lf_top.place(relwidth=1, relheight=1/4,)
    lf_mid = LabelFrame(lf_p, text='mid')
    lf_mid.place(relwidth=1, relheight=2/4, rely=1/4)
    lf_bot = LabelFrame(lf_p, text='bot')
    lf_bot.place(relwidth=1, relheight=1/4, rely=3/4)
    var = StringVar()

    def top_frames(self):
        lf_rom = LabelFrame(self.lf_top)
        lf_rom.place(relwidth=0.6, relheight=1/3, rely=0/3)

        lf_entrada = LabelFrame(self.lf_top)
        lf_entrada.place(relwidth=0.6, relheight=1/3, rely=1/3)

        lf_saida = LabelFrame(self.lf_top)
        lf_saida.place(relwidth=0.6, relheight=1/3, rely=2/3)

        l_rom = Label(lf_rom, text='Romaneio', font=(
            'Segoe UI Semibold', 15))
        l_rom.place(relwidth=1, relheight=1)

        l_entrada = Label(lf_entrada, text='Entrada',
                          font=('Segoe UI Semibold', 15))
        l_entrada.place(relwidth=1, relheight=1)

        l_saida = Label(lf_saida, text='Saída', font=('Segoe UI Semibold', 15))
        l_saida.place(relwidth=1, relheight=1)

        lf_entry_rom = LabelFrame(self.lf_top)
        lf_entry_rom.place(relwidth=0.4, relheight=1/3, relx=0.6)

        lf_entry_entrada = LabelFrame(self.lf_top)
        lf_entry_entrada.place(relwidth=0.4, relheight=1/3, rely=1/3, relx=0.6)

        lf_entry_saida = LabelFrame(self.lf_top)
        lf_entry_saida.place(relwidth=0.4, relheight=1/3, rely=2/3, relx=0.6)

        l_entry_rom = Entry(lf_entry_rom, font=(
            'Segoe UI Semibold', 15), justify='center')
        l_entry_rom.place(relwidth=1, relheight=1)

        lf_entry_entrada = DateEntry(lf_entry_entrada, font=(
            'Segoe UI Semibold', 12), justify='center')
        lf_entry_entrada.place(relwidth=1, relheight=1)

        lf_entry_saida = DateEntry(lf_entry_saida, font=(
            'Segoe UI Semibold', 12), justify='center')
        lf_entry_saida.place(relwidth=1, relheight=1)

    def mid_frames(self):
        pass

    def bot_frames(self):
        pass


if __name__ == '__main__':

    pag = Pagina_1().top_frames()
    app.mainloop()
