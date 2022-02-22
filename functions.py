from tkinter import *
from db_connect import banco_dados
from layout import *

class Function(banco_dados):
    def Botao_limpar(self):
        self.label_chave_acesso.delete(0, END)
        self.respostaHostDB.delete(0, END)
        self.respostaDB.delete(0, END)
        self.respostaUserDB.delete(0, END)
        self.respostaPasswordDB.delete(0, END)
        self.respostaPortDB.delete(0, END)

class loopingChave(Tela):
    def repetidorChaveAcesso(self):
       self.respostaChaveAcesso
       for self.buscaChaveBanco in self.respostaChaveAcesso:
            self.respostaChaveAcesso = self.busca()
            print(self.respostaChaveAcesso) 
            
