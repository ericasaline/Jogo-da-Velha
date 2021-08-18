#from src.model.model import Model 
#from src.controller.controller import Controller 
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class View():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("# JOGO DA VELHA #")

        self.container = tk.Frame(self.root)
        self.container.pack()

        #self.model = Model()
        #self.controller = Controller(self, self.model)

        self.menu()
        self.jogo()
        self.tabuleiro()

        self.line()

        self.root.bind('<Escape>', self.close)
        
        self.root.mainloop()


    # Função encerra o programa
    def close(self, evento):
        sys.exit()


    # Menu com -> Ajuda + Saiba mais
    def menu(self):
        menubar = tk.Menu(self.root) 
        
        self.root.config(menu=menubar)

        fileOp = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label='Opções', menu=fileOp)

        fileOp.add_command(label='Ajuda', command=self.ajuda)
        fileOp.add_command(label='Saiba Mais', command=self.mensagem)


    # Função mostra ajuda ao jogador - message box
    def ajuda(self):
        messagebox.showinfo('AJUDA', '\nPara sair do jogo basta pressionar a tecla ESC \n\n# BOM JOGO! #')


    # Função mostra autor do código - message box
    def mensagem(self):
        messagebox.showinfo('AUTOR', 'Erica Saline')


    # Jogo da Velha - Título
    def jogo(self):
        container = tk.Frame(self.root)
        container.pack()

        game = tk.Label(container, width=30, text='# JOGO DA VELHA #', 
                                   font='loma 18 bold', borderwidth='10', 
                                   bg='cyan', fg='magenta')
        game.grid(column=0, row=0, padx=5, pady=5)


    # Botões - Tabuleiro #
    def tabuleiro(self):
        container = tk.Frame(self.root)
        container.pack()

        # Variável sentinela 
        self.sentinela = tk.IntVar()

        # Variável guarda vencedor (int -> para verificação)
        self.vencedor = tk.IntVar()

        # Variável guarda vitória -> jogador X vs jogador O
        self.vitX = tk.IntVar()
        self.vitO = tk.IntVar()

        # Variável mostra vencedor 
        self.ganhador = tk.StringVar()

        # Variáveis auxiliares para mostrar o número de vitórias de cada jogador
        self.ganhadorX = tk.IntVar()
        self.ganhadorO = tk.IntVar()

        # Variáveis auxiliares - botão posição = bp
        self.bp1 = tk.IntVar()
        self.bp2 = tk.IntVar()
        self.bp3 = tk.IntVar()
        self.bp4 = tk.IntVar()
        self.bp5 = tk.IntVar()
        self.bp6 = tk.IntVar()
        self.bp7 = tk.IntVar()
        self.bp8 = tk.IntVar()
        self.bp9 = tk.IntVar()
        self.bp1 = self.bp2 = self.bp3 = self.bp4 = self.bp5 = self.bp6 = self.bp7 = self.bp8 = self.bp9 = 0

        # Posicionamento dos botões
        # 1   2   3
        # 4   5   6
        # 7   8   9

        # botão = btn (1 2 3 4 5 6 7 8 9)

        # Botão 1 
        self.btn1 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn1.grid(column=0, row=0, padx=5, pady=5)

        # Botão 2
        self.btn2 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn2.grid(column=1, row=0, padx=5, pady=5)

        # Botão 3
        self.btn3 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn3.grid(column=2, row=0, padx=5, pady=5)

        # Botão 4
        self.btn4 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn4.grid(column=0, row=1, padx=5, pady=5)

        # Botão 5
        self.btn5 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn5.grid(column=1, row=1, padx=5, pady=5)

        # Botão 6
        self.btn6 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn6.grid(column=2, row=1, padx=5, pady=5)

        # Botão 7
        self.btn7 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn7.grid(column=0, row=2, padx=5, pady=5)

        # Botão 8
        self.btn8 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn8.grid(column=1, row=2, padx=5, pady=5)

        # Botão 9
        self.btn9 = tk.Button(container, width=6, height=3, text=' ', 
                                        bg='cyan', fg='magenta', font='loma 16 bold')
        self.btn9.grid(column=2, row=2, padx=5, pady=5)


    # Função - label 
    def line(self):
        container = tk.Frame(self.root)
        container.pack()

        self.txtline = tk.Label(container, width=30, text='# '*22, font='loma 18 bold', 
                                        borderwidth='10', bg='cyan', fg='magenta')
        self.txtline.grid(column=0, row=0, padx=5, pady=5)


    # Função reinicializa o jogo
    def novojogo(self):
        self.ganhadorX = self.controller.retornaVX()
        self.ganhadorO = self.controller.retornaVO()
        self.txtline['text'] = (f'# Jogador X - [ {self.ganhadorX} ] vs Jogador O - [ {self.ganhadorO} ] #') 
        self.sentinela = 0
        self.controller.asentinela(self.sentinela)
        self.vencedor = 0
        self.controller.avencedor(self.vencedor)
        self.ganhador = ' '
        self.controller.aganhador(self.ganhador)
        self.btn1['text'] = ' '
        self.bp1 = 0
        self.controller.b1(self.bp1)
        self.btn2['text'] = ' '
        self.bp2 = 0
        self.controller.b2(self.bp2)
        self.btn3['text'] = ' '
        self.bp3 = 0
        self.controller.b3(self.bp3)
        self.btn4['text'] = ' '
        self.bp4 = 0
        self.controller.b4(self.bp4)
        self.btn5['text'] = ' '
        self.bp5 = 0
        self.controller.b5(self.bp5)
        self.btn6['text'] = ' ' 
        self.bp6 = 0
        self.controller.b6(self.bp6)
        self.btn7['text'] = ' '
        self.bp7 = 0
        self.controller.b7(self.bp7)
        self.btn8['text'] = ' '
        self.bp8 = 0
        self.controller.b8(self.bp8)
        self.btn9['text'] = ' '
        self.bp9 = 0
        self.controller.b9(self.bp9)


    # Função encerra o programa
    def close(self, evento):
        sys.exit()
