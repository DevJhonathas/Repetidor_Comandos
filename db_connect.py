import psycopg2

class banco_dados:
    def ConexaoDatabase(self):
        #configuração para conexao do banco
        host = 'localhost'
        dbname = 'teste'
        user = 'postgres'
        password = 'adm8081'
        sslnode = 'requere'

        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslnode = sslnode    
        #string de conexao
        self.conn_string = 'host={0}, dbname={1}, user={2}, password={3}, sslnode={4}'.format
        (self.host, self.dbname, self.user, self.password, self.sslnode)
        self.conn = psycopg2.connect(self.conn_string)
        #Cursor para usar o SQL
        self.cursor =  self.conn.cursor()

    def DesconectaDatabase(self):
        self.conn.close()

    def MontaTabelas(self):
        self.ConexaoDatabase(); print("Conectando ao banco de dados")
        #Criacao da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                comando CHAR(40) NOT NULL,
                chave_acesso FLOAT(20)
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.DesconectaDatabase()