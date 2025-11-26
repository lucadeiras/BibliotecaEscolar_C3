import mysql.connector
from mysql.connector import Error
from pandas import DataFrame
from pathlib import Path
import time


class mySQL_queries:
    """
    Classe para conexão e manipulação de dados no banco MySQL Aiven.
    """

    def __init__(self, can_write: bool = False):
        self.can_write = can_write

        # 🔒 Dados da conexão
        # ATENÇÃO: As credenciais estão aqui, certifique-se de que estão corretas.
        self.host = "mysql-c2-lucasdavi22-6e55.k.aivencloud.com"
        self.port = 19016
        self.database = "biblioteca"
        self.user = "avnadmin"
        self.passwd = "AVNS_SuIzlyyt0jsgcBnycgi"

        # Caminho do certificado SSL
        try:
            base_path = Path(__file__).parent.parent
        except NameError:
            base_path = Path.cwd()

        self.ssl_ca_path = base_path / "conexion" / "passphrase" / "ca.pem"
        self.ssl_ca_str = str(self.ssl_ca_path)

        # print(f"DEBUG: Caminho do CA SSL resolvido: {self.ssl_ca_str}")

        # Inicializa variáveis
        self.conn = None
        self.cur = None

    # ==============================================
    #   CONEXÃO
    # ==============================================
    def connect(self):
        """Tenta conectar ao banco MySQL com timeout e múltiplas tentativas."""
        conn = None
        tentativas = 0
        max_tentativas = 5
        
        print("\n⏳ Tentando conectar ao MySQL Aiven (Timeout: 5s)...")

        while tentativas < max_tentativas:
            try:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.passwd,
                    database=self.database,
                    ssl_ca=self.ssl_ca_str,
                    ssl_verify_identity=True,
                    # 💡 SOLUÇÃO PARA O CONGELAMENTO: Força a falha em 5 segundos
                    connection_timeout=5 
                )

                if self.conn.is_connected():
                    self.cur = self.conn.cursor()
                    print(f"✅ Conexão com o MySQL Aiven ({self.database}) estabelecida com sucesso")
                    return self.conn
                else:
                    print(f"❌ Falha interna ao conectar com o MySQL Aiven. Tentativa {tentativas + 1}/{max_tentativas}.")
                    return None # Sai se a conexão não for estabelecida, mas sem erro.

            except Error as e:
                tentativas += 1
                if tentativas < max_tentativas:
                    print(f"❌ Erro de Conexão ({e.errno}): {e.msg}. Tentativa {tentativas}/{max_tentativas}. Re-tentando em 1s.")
                    time.sleep(1) # Espera antes de tentar novamente
                else:
                    print(f"🔴 Falha final ao conectar ao MySQL Aiven. Último erro: {e}")
                    return None

        return None


    # ==============================================
    #   CONSULTAS (SELECT)
    # ==============================================
    def sqlToDataFrame(self, query: str) -> DataFrame:
        """Executa uma consulta SQL e retorna um DataFrame do pandas."""
        # Note: Este método assume que a conexão já foi estabelecida
        if not self.conn or not self.conn.is_connected():
            raise Exception("Conexão não estabelecida. Chame connect() primeiro.")

        with self.conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [col[0].lower() for col in cur.description]
            return DataFrame(rows, columns=columns)

    # ==============================================
    #   ESCRITA (INSERT, UPDATE, DELETE)
    # ==============================================
    def write(self, query: str, params: tuple = None):
        """Executa comandos INSERT, UPDATE ou DELETE."""
        if not self.can_write:
            raise Exception("Não é possível escrever usando esta conexão (can_write=False).")

        if not self.conn or not self.conn.is_connected():
            raise Exception("Conexão não estabelecida. Chame connect() primeiro.")

        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params or ())
                self.conn.commit()
                print("✅ Comando executado com sucesso!")
                return cur.rowcount
        except Error as e:
            print(f"⚠️ Erro ao executar escrita no banco: {e}")
            self.conn.rollback()
            return 0

    # ==============================================
    #   EXECUÇÃO DE DDL (CREATE, DROP, ALTER)
    # ==============================================
    def executeDDL(self, query: str):
        """Executa comandos DDL como CREATE, DROP, ALTER."""
        return self.write(query)

    # ==============================================
    #   ENCERRAMENTO
    # ==============================================
    def close(self, conn=None):
        """Fecha cursor e conexão com o banco."""
        
        # Prioriza o fechamento da conexão passada como argumento
        conn_to_close = conn if conn else self.conn
        
        if self.cur:
            try:
                self.cur.close()
                self.cur = None
            except Exception:
                pass

        if conn_to_close and conn_to_close.is_connected():
            conn_to_close.close()
            # Se fechar a conexão armazenada, zera ela
        if conn_to_close == self.conn:
             self.conn = None

    def __del__(self):
       try:
          self.close()
       except Exception:
           pass