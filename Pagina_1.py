from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry


class Pagina_1:
    def __init__(self, master):
        self.master = master
    # Listas principais
        self.lista_rom_data = []
        self.lista_entrys = []
        self.lista_codigos = []
        self.var = StringVar()

        lf_p = LabelFrame(master)
        lf_p.place(relwidth=1, relheight=1)
    # Frames principais
        self.lf_top = LabelFrame(lf_p)
        self.lf_top.place(relwidth=1, relheight=0.7/4,)
        self.lf_mid = LabelFrame(lf_p)
        self.lf_mid.place(relwidth=1, relheight=2.7/4, rely=0.7/4)
        self.lf_bot = LabelFrame(lf_p)
        self.lf_bot.place(relwidth=1, relheight=0.5/4, rely=3.5/4)

    def top_frames(self):
        # Frames de posição dos textos "Romaneio", "Entrada", "Saída"
        lf_rom = LabelFrame(self.lf_top)
        lf_rom.place(relwidth=0.6, relheight=1/3, rely=0/3)

        lf_entrada = LabelFrame(self.lf_top)
        lf_entrada.place(relwidth=0.6, relheight=1/3, rely=1/3)

        lf_saida = LabelFrame(self.lf_top)
        lf_saida.place(relwidth=0.6, relheight=1/3, rely=2/3)

        l_rom = Label(lf_rom, text='N° Romaneio', font=(
            'Segoe UI Semibold', 15))
        l_rom.place(relwidth=1, relheight=1)

        l_entrada = Label(lf_entrada, text='Entrada',
                          font=('Segoe UI Semibold', 15))
        l_entrada.place(relwidth=1, relheight=1)

        l_saida = Label(lf_saida, text='Saída', font=('Segoe UI Semibold', 15))
        l_saida.place(relwidth=1, relheight=1)

        # Frames de posição dos widgets que pegam as informações de n° romaneio e data
        lf_entry_rom = LabelFrame(self.lf_top)
        lf_entry_rom.place(relwidth=0.4, relheight=1/3, relx=0.6)

        lf_entry_entrada = LabelFrame(self.lf_top)
        lf_entry_entrada.place(relwidth=0.4, relheight=1/3, rely=1/3, relx=0.6)

        lf_entry_saida = LabelFrame(self.lf_top)
        lf_entry_saida.place(relwidth=0.4, relheight=1/3, rely=2/3, relx=0.6)

        # Campos que pegam as informações de nº romaneio e datas
        l_entry_rom = Entry(lf_entry_rom, font=(
            'Segoe UI Semibold', 15), justify='center')
        l_entry_rom.place(relwidth=1, relheight=1)

        l_entry_entrada = DateEntry(lf_entry_entrada, font=(
            'Segoe UI Semibold', 12), justify='center')
        l_entry_entrada.place(relwidth=1, relheight=1)

        l_entry_saida = DateEntry(lf_entry_saida, font=(
            'Segoe UI Semibold', 12), justify='center')
        l_entry_saida.place(relwidth=1, relheight=1)

        # Adiciona nº do romaneio, data entrda e data saída na lista rom_data
        self.lista_rom_data.append(l_entry_rom)
        self.lista_rom_data.append(l_entry_entrada)
        self.lista_rom_data.append(l_entry_saida)

    def mid_frames(self):
        # Frames para encaixar os widgets
        lb_e = LabelFrame(self.lf_mid, text='Quantidade')
        lb_e.place(relwidth=2/4, relheight=1, relx=2/4,)
        lb_c = LabelFrame(self.lf_mid, text='Código')
        lb_c.place(relwidth=1/4, relheight=1, relx=1/4)
        lb_i = LabelFrame(self.lf_mid, text='Itens')
        lb_i.place(relwidth=1/4, relheight=1, relx=0)
    # Loop para os itens 1~10
        for i in range(10):
            lf = LabelFrame(lb_i)
            lf.place(relwidth=1, relheight=1/10, rely=i/10)
            lb = Label(lf, text=f'Item {i+1}')
            lb.place(relwidth=1, relheight=1)
    # Loop para as quantidades de peças
        for i in range(10):
            inputs = Entry(lb_e)
            inputs.place(relwidth=1, relheight=1/10, relx=0, rely=i/10)
            self.lista_entrys.append(inputs)
    # Loop para os codigos das peças
        for i in range(10):
            cod = Entry(lb_c)
            cod.place(relwidth=1, relheight=1/10, relx=0, rely=i/10)
            self.lista_codigos.append(cod)

    def bot_frames(self):
        # Botão de limpar os campos ACESSA A FUNÇÂO DELETE
        bt_delete = Button(self.lf_bot, text='Limpar', command=delete,
                           font=('Segoe UI Semibold', 12))
        bt_delete.pack(side='left', expand=1)

        # Botão de salvar as informações no arquivo ACESSA A FUNÇÂO SALVAR
        bt_salvar = Button(self.lf_bot, text='Salvar', command=salvar, font=(
            'Segoe UI Semibold', 12))
        bt_salvar.pack(side='right', expand=1)

        # Combobox que guarda a informação dos meses
        lb = LabelFrame(self.lf_bot, text='Mês de Fechamento')
        lb.pack(side='bottom', expand=1)
        combo = ttk.Combobox(lb, textvariable=self.var, font=(
            'Segoe UI Semibold', 12), justify='center', width=8)
        combo.pack(fill='both', expand=1)
        combo['value'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                          'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Função que limpa os campos de digitação de códigos e quantidade de peças


def delete():
    for i in range(10):
        pag_1.lista_entrys[i].delete(0, END)
        pag_1.lista_codigos[i].delete(0, END)

# Salvando em um arquivo txt é temporário, na finalização do projeto isto vai para um bancode dados SQL


def salvar():
    num_rom = []
    for entry in pag_1.lista_rom_data:
        data_rom = entry.get()
        num_rom.append(data_rom)

    if num_rom[0] != '' and pag_1.var.get() != '':
        # salva n° de romaneio e data
        for data in num_rom:
            with open(f'Romaneio {num_rom[0]}.txt', 'a') as arq:
                arq.write(f'{data}\n')

        # salva codigo das peças
        for codigos in pag_1.lista_codigos:
            cod = codigos.get()
            if cod == '':
                cod = 0
            with open(f'Romaneio {num_rom[0]}.txt', 'a') as arq:
                arq.write(f'{cod}\n')

        # salva quantidade de peças
        for qntd in pag_1.lista_entrys:
            quantidade = qntd.get()
            if quantidade == '':
                quantidade = 0
            with open(f'Romaneio {num_rom[0]}.txt', 'a') as arq:
                arq.write(f'{quantidade}\n')
        # salva mês do fechamento do lote
        with open(f'Romaneio {num_rom[0]}.txt', 'a') as arq:
            arq.write(f'{pag_1.var.get()}\n')


if __name__ == '__main__':
    app = Tk()

    app.geometry('300x500')
    pag_1 = Pagina_1(app)
    pag_1.top_frames()
    pag_1.mid_frames()
    pag_1.bot_frames()
    app.mainloop()
