from cProfile import label
from cgitb import text
from distutils import command
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import Toplevel
from db_connect import banco_dados
from functions import Function
from LayoutDB import *


class Tela(Function, banco_dados):
    def Configuracao_tela(self):
        self.root.title("Repetidor de comandos")
        self.root.iconbitmap("Image/database.ico")
        self.root.minsize(width=535, height=530)
        self.root.geometry("400x400+350+100")
        self.root.resizable(False, False)
        self.root.configure(background="#1e90ff")

    def Frames_tela(self):
        self.PrimeiraTelaFrame = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.PrimeiraTelaFrame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
        
        self.PrimeiraTelaFrame2 = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.PrimeiraTelaFrame2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)       
    
    def Botoes_Primeiro_frames(self):
        #criação botão de limpar(todos os comandos escritos)
        self.button_limpar = Button(self.PrimeiraTelaFrame, text="Limpar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''), command=self.Botao_limpar)
        self.button_limpar.place(relx=0.23, rely=0.28, relwidth=0.14, relheight=0.13)
        #criação botão de enviar(inseri no banco automáticamente)
        self.button_enviar = Button(self.PrimeiraTelaFrame, text="Enviar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_enviar.place(relx=0.69, rely=0.28, relwidth=0.14, relheight=0.13)
        #criação botão de novo(abre a janela para por o comando)
        self.button_banco = Button(self.PrimeiraTelaFrame, text="Banco", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''), command=self.telaBancoConfig)
        self.button_banco.place(relx=0.85, rely=0.01, relwidth=0.12, relheight=0.12)
        #criação botão de altera(no banco)
        self.button_alterar = Button(self.PrimeiraTelaFrame, text="Alterar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_alterar.place(relx=0.85, rely=0.15, relwidth=0.12, relheight=0.12)
        #criação botão de buscar (no banco)
        self.button_buscar = Button(self.PrimeiraTelaFrame, text="Buscar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_buscar.place(relx=0.23, rely=0.15, relwidth=0.6, relheight=0.12)
   
    def LabelPrimeiraTelaFrame(self):
        #Criação Label e entrada do código
        self.label_chave_acesso = Label(self.PrimeiraTelaFrame, text="Chave_acesso:", bd=3, background='#87ceeb', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_chave_acesso.place(relx=0.02, rely=0.01, relwidth=0.2, relheight=0.12)
        self.label_chave_acesso = Entry(self.PrimeiraTelaFrame, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_chave_acesso.place(relx=0.23, rely=0.01, relwidth=0.6, relheight=0.12)
   
    def ListaPrimeiraTelaFrame2(self):
        #Lista no qual irar ficar os resultados do looping das label
        self.Lista = ttk.Treeview(self.PrimeiraTelaFrame2, height=3, columns=("Comando", "chave_acesso"))
        self.Lista.heading("#0", text="")
        self.Lista.heading("#1", text="Comando")
        self.Lista.heading("#2", text="Chave_acesso")

        self.Lista.column("#0", width=1)
        self.Lista.column("#1", width=100)
        self.Lista.column("#2", width=300)

        self.Lista.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)
        #Criação do scrollbar da lista
        self.Scroll_lista = Scrollbar(self.PrimeiraTelaFrame2, orient='vertical')
        self.Lista.configure(yscroll=self.Scroll_lista.set)
        self.Scroll_lista.place(relx=0.96, rely=0.015, relwidth=0.04, relheight=0.85)