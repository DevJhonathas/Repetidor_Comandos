from tkinter import *
from db_connect import banco_dados

class Function(banco_dados):
    def Botao_limpar(self):
        self.label_chave_acesso.delete(0, END)
    
    
