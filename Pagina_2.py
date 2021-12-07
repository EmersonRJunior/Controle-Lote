from tkinter import *
from tkinter import ttk
import glob


class Pagina_2:
    def __init__(self, master):
        self.list_mes = StringVar()
        self.list_empresa = StringVar()

        # Frames principais
        self.lf_top = LabelFrame(master, text='top')
        self.lf_top.place(relwidth=1, relheight=1/5)
        self.lf_mid = LabelFrame(master, text='mid')
        self.lf_mid.place(relwidth=1, relheight=3/5, rely=1/5)
        self.lf_bot = LabelFrame(master, text='bottom')
        self.lf_bot.place(relwidth=1, relheight=1/5, rely=4/5)

    def top_frames(self):
        # Frames e Labels esquerdos / de texto
        lf_mes = LabelFrame(self.lf_top)
        lf_mes.place(relwidth=0.3, relheight=1/2, relx=0.1)

        lf_empresa = LabelFrame(self.lf_top)
        lf_empresa.place(relwidth=0.3, relheight=1/2, relx=0.1, rely=1/2)

        l_mes = Label(lf_mes, text='Mês', font=(
            'Segoe UI Semibold', 12), justify='center')
        l_mes.pack(fill='both', expand=1)

        lf_empresa = Label(lf_empresa, text='Empresa', font=(
            'Segoe UI Semibold', 12), justify='center')
        lf_empresa.pack(fill='both', expand=1)
        # Frames direitos / comboboxes
        lf_combo_mes = LabelFrame(self.lf_top, text='Mês do Fechamento')
        lf_combo_mes.place(relwidth=0.5, relheight=1/2, relx=0.45, rely=-0.1/2)

        lf_combo_empresa = LabelFrame(
            self.lf_top, text='Empresa de Fechamento')
        lf_combo_empresa.place(
            relwidth=0.5, relheight=1/2, relx=0.45, rely=0.9/2)

        combo_mes = ttk.Combobox(lf_combo_mes, textvariable=self.list_mes, font=(
            'Segoe UI Semibold', 12), justify='center')
        combo_mes.pack(fill='both', expand=1)
        combo_mes['value'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

        combo_empresa = ttk.Combobox(
            lf_combo_empresa, textvariable=self.list_empresa, font=(
                'Segoe UI Semibold', 12), justify='center')
        combo_empresa.pack(fill='both', expand=1)
        combo_empresa['value'] = ('Composê', 'Quebra-Cabeça')


if __name__ == '__main__':
    app = Tk()
    app.geometry('300x500')
    pag_2 = Pagina_2(app)
    pag_2.top_frames()
    app.mainloop()
