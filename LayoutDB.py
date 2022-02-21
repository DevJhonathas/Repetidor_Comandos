from cProfile import label
from cgitb import text
from distutils import command
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import Toplevel
from db_connect import banco_dados
from functions import Function

class SegundaTelaBanco(Function):
    def telaBancoConfig(self):
        self.root2 = Toplevel()
        self.configLabel()
        self.botoesSegundaTela()
        self.root2.iconbitmap("Image/database.ico")
        self.root2.title("Configuração do banco")
        self.root2.configure(background = '#87ceeb')
        self.root2.geometry('300x200+350+100')
        self.root2.resizable(True, True)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def configLabel(self):
        #Host
        self.labelHostDB = Label(self.root2, text="Host:", fg='black', bg='#87ceeb',
                                    font= ('verdana', '8', 'bold'))
        self.labelHostDB.place(relx=0.11, rely=0.01, relwidth=0.2, relheight=0.1)
        self.respostaHostDB = Entry(self.root2, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.respostaHostDB.place(relx=0.35, rely=0.01, relwidth=0.5, relheight=0.1)
        #Database
        self.respostaDB = Entry(self.root2, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.respostaDB.place(relx=0.35, rely=0.15, relwidth=0.5, relheight=0.1)
        self.labelDB = Label(self.root2, text="DataBase:", fg='black', background='#87ceeb',
                                    font= ('verdana', '8', 'bold'))
        self.labelDB.place(relx=0.02, rely=0.15, relwidth=0.3, relheight=0.1)
        #Usuario
        self.labelUserDB  = Label(self.root2, text="Usuário:", fg='black', background='#87ceeb',
                                    font= ('verdana', '8', 'bold'))
        self.labelUserDB.place(relx=0.02, rely=0.3, relwidth=0.3, relheight=0.1)
        self.respostaUserDB = Entry(self.root2, bd=2, bg='white', fg='black', background="white", 
                                    font= ('verdana', '8', 'bold'))
        self.respostaUserDB.place(relx=0.35, rely=0.3, relwidth=0.5, relheight=0.1)
        #Password
        self.labelPasswordDB  = Label(self.root2, text="Password:", fg='black', background='#87ceeb',
                                    font= ('verdana', '8', 'bold'))
        self.labelPasswordDB.place(relx=0.02, rely=0.45, relwidth=0.3, relheight=0.1)
        self.respostaPasswordDB = Entry(self.root2, bd=2, bg='white', fg='black', background="white", 
                                    font= ('verdana', '8', 'bold'))
        self.respostaPasswordDB.place(relx=0.35, rely=0.45, relwidth=0.5, relheight=0.1)
        #Port
        self.labelPortDB  = Label(self.root2, text="Porta:", fg='black', background='#87ceeb',
                                    font= ('verdana', '8', 'bold'))
        self.labelPortDB.place(relx=0.02, rely=0.6, relwidth=0.3, relheight=0.1)
        self.respostaPortDB = Entry(self.root2, bd=2, bg='white', fg='black', background="white", 
                                    font= ('verdana', '8', 'bold'))
        self.respostaPortDB.place(relx=0.35, rely=0.6, relwidth=0.5, relheight=0.1)
    
    def botoesSegundaTela(self):
        self.button_limpar = Button(self.root2, text="Limpar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''), command=self.Botao_limpar)
        self.button_limpar.place(relx=0.2, rely=0.84, relwidth=0.3, relheight=0.12)
        self.button_alterar = Button(self.root2, text="Confirmar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_alterar.place(relx=0.6, rely=0.84, relwidth=0.3, relheight=0.12)