from tkinter import font
import pandas as pd
import os
from tkinter import *

root = Tk()
class tela:
    def __init__(self):
        self.root = root
        self.Configuracao_tela()
        self.Frames_tela()
        self.Widgets_Primeiro_frames()
        self.root.mainloop()
    
    def Configuracao_tela(self):
        self.root.title("Repetidor de comandos")
        self.root.iconbitmap("Image/database.ico")
        self.root.maxsize(width=700, height=600)
        self.root.minsize(width=300, height=400)
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        self.root.configure(background="#191919")

    def Frames_tela(self):
        self.Primeiro_frame = Frame(self.root, bd=4, bg="#1e1e1e")
        self.Primeiro_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
        
        self.Segundo_frame = Frame(self.root, bd=4, bg="#1e1e1e")
        self.Segundo_frame.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)       
    
    def Widgets_Primeiro_frames(self):
        #criação botão de limpar(todos os comandos escritos)
        self.button_limpar = Button(self.Primeiro_frame, text="Limpar", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.button_limpar.place(relx=0.001, rely=0.9, relwidth=0.2, relheight=0.12)
        #criação botão de enviar(inseri no banco automáticamente)
        self.button_limpar = Button(self.Primeiro_frame, text="Enviar", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.button_limpar.place(relx=0.001, rely=0.77, relwidth=0.2, relheight=0.12)
        #criação botão de novo(abre a janela para por o comando)
        self.button_limpar = Button(self.Primeiro_frame, text="Novo", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.button_limpar.place(relx=0.8, rely=0.77, relwidth=0.2, relheight=0.12)
        #criação botão de altera(no banco)
        self.button_limpar = Button(self.Primeiro_frame, text="Alterar", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.button_limpar.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.12)
        #criação botão de buscar (no banco)
        self.button_limpar = Button(self.Primeiro_frame, text="Buscar", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.button_limpar.place(relx=0.05, rely=0.15, relwidth=0.81, relheight=0.12)

        #Criação Label e entrada do código
        self.label_codigo = Label(self.Primeiro_frame, text="Código:", bd=3, bg='#323232', fg='white', 
                                    font= ('verdana', '8', 'bold'))
        self.label_codigo.place(relx=0.05, rely=0.01, relwidth=0.2, relheight=0.12)

        self.codigo_entry = Entry(self.Primeiro_frame)
        self.codigo_entry.place(relx=0.256, rely=0.01, relwidth=0.6, relheight=0.12)

tela()