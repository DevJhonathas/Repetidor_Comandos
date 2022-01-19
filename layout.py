from tkinter import font
import pandas as pd
import os
from tkinter import *
from tkinter import ttk

root = Tk()
class tela:
    def __init__(self): #Classe iniciadora
        self.root = root
        self.Configuracao_tela()
        self.Frames_tela()
        self.Botoes_Primeiro_frames()
        self.Label_primeiro_frame()
        self.Lista_segundo_frame()
        self.root.mainloop()
    
    def Configuracao_tela(self):
        self.root.title("Repetidor de comandos")
        self.root.iconbitmap("Image/database.ico")
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=535, height=530)
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        self.root.configure(background="#1e90ff")

    def Frames_tela(self):
        self.Primeiro_frame = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.Primeiro_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
        
        self.Segundo_frame = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.Segundo_frame.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)       
    
    def Botoes_Primeiro_frames(self):
        #criação botão de limpar(todos os comandos escritos)
        self.button_limpar = Button(self.Primeiro_frame, text="Limpar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_limpar.place(relx=0.23, rely=0.45, relwidth=0.14, relheight=0.13)
        #criação botão de enviar(inseri no banco automáticamente)
        self.button_limpar = Button(self.Primeiro_frame, text="Enviar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_limpar.place(relx=0.69, rely=0.45, relwidth=0.14, relheight=0.13)
        #criação botão de novo(abre a janela para por o comando)
        self.button_limpar = Button(self.Primeiro_frame, text="Novo", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_limpar.place(relx=0.85, rely=0.01, relwidth=0.12, relheight=0.12)
        #criação botão de altera(no banco)
        self.button_limpar = Button(self.Primeiro_frame, text="Alterar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_limpar.place(relx=0.85, rely=0.15, relwidth=0.12, relheight=0.12)
        #criação botão de buscar (no banco)
        self.button_limpar = Button(self.Primeiro_frame, text="Buscar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_limpar.place(relx=0.23, rely=0.3, relwidth=0.6, relheight=0.12)

    def Label_primeiro_frame(self):
        #Criação Label e entrada do código
        self.label_codigo = Label(self.Primeiro_frame, text="Comando:", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.01, relwidth=0.2, relheight=0.12)
        self.codigo_entry = Entry(self.Primeiro_frame, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.codigo_entry.place(relx=0.23, rely=0.01, relwidth=0.6, relheight=0.12)

        self.label_codigo = Label(self.Primeiro_frame, text="Chave_acesso:", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.15, relwidth=0.2, relheight=0.12)
        self.codigo_entry = Entry(self.Primeiro_frame, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.codigo_entry.place(relx=0.23, rely=0.15, relwidth=0.6, relheight=0.12)

    def Lista_segundo_frame(self):
        #Lista no qual irar ficar os resultados do looping das label
        self.Lista = ttk.Treeview(self.Segundo_frame, height=3, columns=("Comando", "chave_acesso"))
        self.Lista.heading("#0", text="")
        self.Lista.heading("#1", text="Comando")
        self.Lista.heading("#2", text="Chave_acesso")

        self.Lista.column("#0", width=1)
        self.Lista.column("#1", width=100)
        self.Lista.column("#2", width=300)

        self.Lista.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)
tela()