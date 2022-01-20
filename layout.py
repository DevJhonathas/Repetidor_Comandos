from tkinter import font
from tkinter import *
from tkinter import ttk
from db_connect import banco_dados

root = Tk()
class Function():
    def Botao_limpar(self):
        self.label_comando.delete(0, END)
        self.label_chave_acesso.delete(0, END)
        

class Tela(Function, banco_dados):
    def __init__(self): #Classe iniciadora
        self.root = root
        self.Configuracao_tela()
        self.Frames_tela()
        self.Botoes_Primeiro_frames()
        self.Label_primeiro_frame()
        self.Lista_segundo_frame()
        self.MontaTabelas()
        self.root.mainloop()
    
    def Configuracao_tela(self):
        self.root.title("Repetidor de comandos")
        self.root.iconbitmap("Image/database.ico")
        self.root.minsize(width=535, height=530)
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(background="#1e90ff")

    def Frames_tela(self):
        self.Primeiro_frame = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.Primeiro_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
        
        self.Segundo_frame = Frame(self.root, bd=4, bg="#87ceeb", highlightbackground="#888888", highlightthickness=2)
        self.Segundo_frame.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)       
    
    def Botoes_Primeiro_frames(self):
        #criação botão de limpar(todos os comandos escritos)
        self.button_limpar = Button(self.Primeiro_frame, text="Limpar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''), command=self.Botao_limpar)
        self.button_limpar.place(relx=0.23, rely=0.45, relwidth=0.14, relheight=0.13)
        #criação botão de enviar(inseri no banco automáticamente)
        self.button_enviar = Button(self.Primeiro_frame, text="Enviar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_enviar.place(relx=0.69, rely=0.45, relwidth=0.14, relheight=0.13)
        #criação botão de novo(abre a janela para por o comando)
        self.button_novo = Button(self.Primeiro_frame, text="Novo", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_novo.place(relx=0.85, rely=0.01, relwidth=0.12, relheight=0.12)
        #criação botão de altera(no banco)
        self.button_alterar = Button(self.Primeiro_frame, text="Alterar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_alterar.place(relx=0.85, rely=0.15, relwidth=0.12, relheight=0.12)
        #criação botão de buscar (no banco)
        self.button_buscar = Button(self.Primeiro_frame, text="Buscar", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', ''))
        self.button_buscar.place(relx=0.23, rely=0.3, relwidth=0.6, relheight=0.12)

    def Label_primeiro_frame(self):
        #Criação Label e entrada do código
        self.label_comando = Label(self.Primeiro_frame, text="Comando:", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_comando.place(relx=0.02, rely=0.01, relwidth=0.2, relheight=0.12)
        self.label_comando = Entry(self.Primeiro_frame, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_comando.place(relx=0.23, rely=0.01, relwidth=0.6, relheight=0.12)

        self.label_chave_acesso = Label(self.Primeiro_frame, text="Chave_acesso:", bd=3, bg='#dddddd', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_chave_acesso.place(relx=0.02, rely=0.15, relwidth=0.2, relheight=0.12)
        self.label_chave_acesso = Entry(self.Primeiro_frame, bd=2, bg='white', fg='black', 
                                    font= ('verdana', '8', 'bold'))
        self.label_chave_acesso.place(relx=0.23, rely=0.15, relwidth=0.6, relheight=0.12)

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
        #Criação do scrollbar da lista
        self.Scroll_lista = Scrollbar(self.Segundo_frame, orient='vertical')
        self.Lista.configure(yscroll=self.Scroll_lista.set)
        self.Scroll_lista.place(relx=0.96, rely=0.015, relwidth=0.04, relheight=0.85)
Tela()