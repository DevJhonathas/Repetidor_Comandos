from ssl import cert_time_to_seconds
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class banco_dados:
    def ConexaoDatabase(self):
        #configuração para conexao do banco
        self.engine = create_engine('postgresql://postgres:(adm8081)@192.168.0.13:5433/teste')
        #Cursor para usar o SQL
        self.cursor =  self.engine.cursor()

    def DesconectaDatabase(self):
        self.engine.close()

    def MontaTabelas(self):
        self.ConexaoDatabase(); print("Conectando ao banco de dados")
        #Criacao da tabela
        self.sql("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                comando CHAR(40) NOT NULL,
                chave_acesso FLOAT(20)
                );
            """)
        self.engine.commit()
        self.DesconectaDatabase()
