from ssl import cert_time_to_seconds
import psycopg2
import pandas as pd


class banco_dados:
    def ConexaoDatabase(self):
        #configuração para conexao do banco
        self.connection = psycopg2.connect(user = "postgres", password = "(adm8081)", host = "localhost", port = "5433")
        #Cursor para usar o SQL
        self.cursor = self.connection.cursor()

    def DesconectaDatabase(self):
        self.connection.close()

    def MontaTabelas(self):
        self.ConexaoDatabase(); print("Conectando ao banco de dados")
        #Criacao da tabela
        self.Sql_Insert = ("""
            CREATE public clientes(
                cod INTEGER PRIMARY KEY,
                comando CHAR(40) NOT NULL,
                chave_acesso INTEGER(20)
                );
            """)
        self.cursor.execute(self.Sql_Insert)
        self.connection.commit()
        self.DesconectaDatabase()
