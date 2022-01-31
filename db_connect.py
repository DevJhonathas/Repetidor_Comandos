import psycopg2
from layout import *

class banco_dados:
    def ConexaoDatabase(self):
        #configuração para conexao do banco
        self.connection = psycopg2.connect(host = "localhost", database= "Teste_programa", user = "postgres", password = "(adm8081)", port = "5433")
        #Cursor para usar o SQL
        self.cursor = self.connection.cursor()
    def DesconectaDatabase(self):
        self.connection.close() 
    def MontaTabelas(self):
        self.ConexaoDatabase(); print("Conectando ao banco de dados")
        #Criacao da tabela
        self.Sql_Insert = ("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INT PRIMARY KEY,
                comando VARCHAR(40) NOT NULL,
                chave_acesso INT
                );
            """) #Criação da tabela 
        self.cursor.execute(self.Sql_Insert)
        self.connection.commit()
        self.DesconectaDatabase()
    def select_tebela(self): #seleção na tabela  
        self.busca = ("""
                      Select * from clientes
                      """)
        self.cursor.execute(self.Sql_Insert)
        self.connection.commit()
        self.DesconectaDatabase()