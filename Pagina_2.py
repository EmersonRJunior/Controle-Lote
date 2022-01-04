from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import glob
import os


class Pagina_2:
    def __init__(self, master):
        self.master = master
        self.list_mes = StringVar()
        self.list_empresa = StringVar()
        self.scrolledtext = []
        self.list_romaneio = []
        self.list_romaneio_var = StringVar()

        # Frames principais
        self.lf_top = LabelFrame(master)
        self.lf_top.place(relwidth=1, relheight=1/5)
        self.lf_mid = LabelFrame(master)
        self.lf_mid.place(relwidth=1, relheight=3/5, rely=1/5)
        self.lf_bot = LabelFrame(master)
        self.lf_bot.place(relwidth=1, relheight=1/5, rely=4/5)

    def salvar(self):
        st = self.scrolledtext[0].get('1.0', END)
        with open('text.txt', 'a') as file:
            file.write(st)

    def gerar(self):
        self.list_romaneio.clear()
        mes = self.list_mes.get()
        empresa = self.list_empresa.get()
        for x in glob.glob(f'Fechamentos/{empresa}/{mes}/*'):
            romaneio = (os.path.basename(x))
            self.list_romaneio.append(os.path.splitext(romaneio)[0])

        if len(self.list_romaneio) <= 10:
            qntd_labels = 10
        elif len(self.list_romaneio) > 10:
            qntd_labels = len(self.list_romaneio)

        for i in range(len(self.list_romaneio)):
            romaneio = LabelFrame(self.lf_romaneio)
            romaneio.place(relwidth=1, relheight=1 /
                           qntd_labels, rely=i/qntd_labels)
            lb_romaneio = Label(romaneio, text=self.list_romaneio[i])
            lb_romaneio.pack(fill='both', expand=1)

    def top_frames(self):
        # Frames e Labels esquerdos / de texto
        lf_mes = LabelFrame(self.lf_top)
        lf_mes.place(relwidth=0.2, relheight=1/2, relx=0.05)

        lf_empresa = LabelFrame(self.lf_top)
        lf_empresa.place(relwidth=0.2, relheight=1/2, rely=1/2, relx=0.05)

        l_mes = Label(lf_mes, text='Mês', font=(
            'Segoe UI Semibold', 12), justify='center')
        l_mes.pack(fill='both', expand=1)

        l_empresa = Label(lf_empresa, text='Empresa', font=(
            'Segoe UI Semibold', 12), justify='center')
        l_empresa.pack(fill='both', expand=1)

        # Frames direitos / comboboxes
        lf_combo_mes = LabelFrame(self.lf_top, text='Mês do Fechamento')
        lf_combo_mes.place(relwidth=0.5, relheight=1/2, relx=0.3, rely=-0.1/2)

        lf_combo_empresa = LabelFrame(
            self.lf_top, text='Empresa de Fechamento')
        lf_combo_empresa.place(
            relwidth=0.5, relheight=1/2, relx=0.3, rely=0.9/2)

        lf_botao_gerar = LabelFrame(self.lf_top)
        lf_botao_gerar.place(relwidth=0.15, relheight=3 /
                             4, relx=0.825, rely=0.1)

        combo_mes = ttk.Combobox(lf_combo_mes, textvariable=self.list_mes, font=(
            'Segoe UI Semibold', 18), justify='center')
        combo_mes.pack(fill='both', expand=1)
        combo_mes['value'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

        combo_empresa = ttk.Combobox(
            lf_combo_empresa, textvariable=self.list_empresa, font=(
                'Segoe UI Semibold', 18), justify='center')
        combo_empresa.pack(fill='both', expand=1)
        combo_empresa['value'] = ('Composê', 'Quebra-Cabeça')

        b_botao_gerar = Button(lf_botao_gerar, text='Gerar \n Fechamento', font=(
            'Segoe UI Semibold', 12), justify='center', command=self.gerar).pack(fill='both', expand=1)

    def mid_frames(self):
        # Iniciando os frames de posição
        self.lf_romaneio = LabelFrame(self.lf_mid, text='Romaneios')
        self.lf_romaneio.place(relwidth=3/10, relheight=1)

        lf_qntd = LabelFrame(self.lf_mid, text='Qntd')
        lf_qntd.place(relwidth=2/10, relheight=1, relx=3/10)

        lf_preço = LabelFrame(self.lf_mid, text='  R$')
        lf_preço.place(relwidth=1.5/10, relheight=1, relx=5/10)

        lf_entrada = LabelFrame(self.lf_mid, text='Entrada')
        lf_entrada.place(relwidth=2/10, relheight=1, relx=6.5/10)

        lf_saida = LabelFrame(self.lf_mid, text='saída')
        lf_saida.place(relwidth=1.5/10, relheight=1, relx=8.5/10)
        # Widgets

    def bot_frames(self):
        lb = LabelFrame(self.lf_bot, text='Obs:')
        lb.place(relwidth=0.5, relheight=1)
        st = scrolledtext.ScrolledText(lb, wrap=WORD)
        st.place(relwidth=1, relheight=1)

        Button(self.lf_bot, text='teste',
               command=self.salvar).pack(side='right')
        self.scrolledtext.append(st)


if __name__ == '__main__':
    app = Tk()
    app.geometry('670x750')
    pag_2 = Pagina_2(app)
    pag_2.top_frames()
    pag_2.mid_frames()
    pag_2.bot_frames()
    app.mainloop()
