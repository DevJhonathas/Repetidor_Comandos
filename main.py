from layout import Tela
from db_connect import *
from functions import *
from LayoutDB import SegundaTelaBanco

root = Tk()
class Construtor(Tela, SegundaTelaBanco):
    def __init__(self): #Classe construtora
        self.root = root
        self.Configuracao_tela()
        self.Frames_tela()
        self.Botoes_Primeiro_frames()
        self.LabelPrimeiraTelaFrame()
        self.ListaPrimeiraTelaFrame2()
        self.MontaTabelas()
        self.root.mainloop()
Construtor()