from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import os
from Pagina_2 import Pagina_2


class Pagina_1:
    def __init__(self, master):
        self.master = master
        # Listas principais
        self.lista_rom_data = []
        self.lista_entrys = []
        self.lista_codigos = []
        self.var = StringVar()
        self.var_e = StringVar()

        lf_p = LabelFrame(master)
        lf_p.place(relwidth=1, relheight=1)
        # Frames principais
        self.lf_top = LabelFrame(lf_p)
        self.lf_top.place(relwidth=1, relheight=0.7/4,)
        self.lf_mid = LabelFrame(lf_p)
        self.lf_mid.place(relwidth=1, relheight=2.7/4, rely=0.7/4)
        self.lf_bot = LabelFrame(lf_p)
        self.lf_bot.place(relwidth=1, relheight=0.5/4, rely=3.5/4)

    # Funções dos botões
    def delete(self):
        for i in range(10):
            self.lista_rom_data[0].delete(0, END)
            self.lista_entrys[i].delete(0, END)
            self.lista_codigos[i].delete(0, END)

    def salvar(self):
        # inicio funçao salvar
        numero_romaneio = []
        for num_entr_saida in self.lista_rom_data:  # coleta numero do romaneio, data de entrada e data de saida
            data_rom = num_entr_saida.get()
            numero_romaneio.append(data_rom)

        # recebe informações
        mes_empresa = [self.var.get(), self.var_e.get()]
        mes = mes_empresa[0]
        empresa = mes_empresa[1]
        romaneio = numero_romaneio[0]
        entrada = numero_romaneio[1]
        saida = numero_romaneio[2]
        qntd_list = []
        cod_list = []
        lista_cod_excel = []
        lista_preço_excel = []
        verificar = []
        codigo_existe = True

        # puxa as informações do excel
        import pandas as pd
        excel = pd.read_excel('Preço_peças.xlsx', dtype=str)
        cod_excel = excel['codigo']
        preço_excel = excel['preço']
        lista_cod_excel.append(cod_excel)
        lista_preço_excel.append(preço_excel)

        # puxa codigo das peças
        for codigos in self.lista_codigos:
            cod = codigos.get()
            if cod == '':
                cod = '0'
            cod_list.append(cod)

        # puxa quantidade de peças
        for qntd in self.lista_entrys:
            quantidade = qntd.get()
            if quantidade == '':
                quantidade = '0'
            qntd_list.append(quantidade)

        # verifica se o valor dos codigos no app não é zero
        for i in range(10):
            if cod_list[i] != '0' and qntd_list[i] != '0':
                verificar.append(True)
            elif cod_list[i] == '0' and qntd_list[i] == '0':
                verificar.append(True)
            elif cod_list[i] == '0' and qntd_list[i] != '0':
                verificar.append(False)
            elif cod_list[i] != '0' and qntd_list[i] == '0':
                verificar.append(False)

        # deveria verificar se o codigo digitado existe na planilha
        for i in range(10):
            if not cod_list[i] in cod_excel and False in verificar:
                codigo_existe = False

        # Reúne todas as informações e salva em um excel apenas se nao houver informações importantes em branco
        if romaneio != '' and self.var.get() != '' and self.var_e.get() != '':
            # verifica se existe a pasta da empresa e mês de fechamento, senão, cria ambas
            if not False in verificar and codigo_existe == True:
                path_rom = (f'Fechamentos/{empresa}/{mes}')
                if not os.path.isdir(path_rom):
                    os.makedirs(path_rom)

                dados = {
                    'Item': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                    'Código': cod_list,
                    'Quantidade': qntd_list,
                    'Entrada': entrada,
                    'Saída': saida
                }
                df = pd.DataFrame.from_dict(dados)
                df.to_excel(
                    f'{path_rom}/Romaneio {romaneio}.xlsx', 'fechamento', index=False)
                print(df.loc['130', 'Quantidade'])

            else:
                print('Verifique se os codigos estão \npreenchidos ou se estão corretos')
        else:
            print(
                'Verifique se preencheu as colunas n° romaneio,\nempresa e mes de fechamento')

    def change_window(self):
        top = Toplevel()
        pag_2 = Pagina_2(top)
        top.geometry('700x600')
        pag_2.top_frames()
        pag_2.mid_frames()
        pag_2.bot_frames()
        top.mainloop()

    # Corpo do aplicativo
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
            inputs = Entry(lb_e, justify='center')
            inputs.place(relwidth=1, relheight=1/10, relx=0, rely=i/10)
            self.lista_entrys.append(inputs)
        # Loop para os codigos das peças
        for i in range(10):
            cod = Entry(lb_c, justify='center')
            cod.place(relwidth=1, relheight=1/10, relx=0, rely=i/10)
            self.lista_codigos.append(cod)

    def bot_frames(self):
        # Frame dos botões
        f_bt = LabelFrame(self.lf_bot)
        f_bt.place(relwidth=0.3, relheight=0.8, relx=0.7, rely=0.1)

        # Botão de limpar os campos ACESSA A FUNÇÂO DELETE
        bt_delete = Button(f_bt, text='Limpar', command=self.delete,
                           font=('Segoe UI Semibold', 9))
        bt_delete.place(relwidth=0.5, relheight=0.5, relx=0.5)

        # Botão de salvar as informações no arquivo ACESSA A FUNÇÂO SALVAR
        bt_salvar = Button(f_bt, text='Salvar', command=self.salvar, font=(
            'Segoe UI Semibold', 10))
        bt_salvar.place(relwidth=0.5, relheight=0.5)

        # Botao que abre a janela pra gerar o fechamento (Pagina 2)
        bt_gerar_fechamento = Button(
            f_bt, text='Gerar Fechamento', command=self.change_window)
        bt_gerar_fechamento.place(relwidth=1, relheight=0.5, rely=0.5)

        lb = LabelFrame(
            self.lf_bot, text=' Fechamento                    Empresa')
        lb.place(relwidth=0.7, relheight=0.9)

        # Combobox que guarda a informação dos meses
        combo = ttk.Combobox(lb, textvariable=self.var, font=(
            'Segoe UI Semibold', 12), justify='center', width=8)
        combo.pack(side='left', expand=1)

        combo['value'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                          'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

        # Combobox que guarda a informação das empresas
        combo_e = ttk.Combobox(lb, textvariable=self.var_e, font=(
            'Segoe UI Semibold', 12), justify='center', width=8)
        combo_e.pack(side='right', expand=1)

        combo_e['values'] = ('Composê', 'Quebra-Cabeça')


if __name__ == '__main__':
    app = Tk()

    app.geometry('370x550')
    pag_1 = Pagina_1(app)
    pag_1.top_frames()
    pag_1.mid_frames()
    pag_1.bot_frames()
    app.mainloop()
