from layout import *
from db_connect import *

class iniciador:
    def __init__(self): #Classe iniciadora
        self.root = root
        self.Configuracao_tela()
        self.Frames_tela()
        self.Botoes_Primeiro_frames()
        self.Label_primeiro_frame()
        self.Lista_segundo_frame()
        #self.MontaTabelas()
        self.root.mainloop()
iniciador()