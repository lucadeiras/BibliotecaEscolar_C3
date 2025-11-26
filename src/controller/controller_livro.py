import mysql.connector
from src.model.livro import Livro
from src.conexion.mySQL_queries import mySQL_queries


class ControllerLivro:
    def __init__(self):
        self.mysql = mySQL_queries()

    # ---------------- INSERIR LIVRO ----------------
    def inserir(self, livro: Livro):
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()

            sql = """
                INSERT INTO livro (
                    genero, titulo, autor, editora, ano_publicacao,
                    localizacao, num_paginas, estoque, disponivel
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                livro.get_genero(),
                livro.get_titulo(),
                livro.get_autor(),
                livro.get_editora(),
                livro.get_ano_publicacao(),
                livro.get_localizacao(),
                livro.get_num_paginas(),
                livro.get_estoque(),
                int(livro.get_disponivel())
            )
            cursor.execute(sql, valores)
            conn.commit()
            print(" Livro inserido com sucesso!")
        except mysql.connector.Error as err:
            print(f" Erro ao inserir livro: {err}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ---------------- ATUALIZAR LIVRO (INTERATIVO) ----------------
    def atualizar(self):
        conn = None
        cursor = None
        try:
            id_livro = input("Informe o ID do livro que deseja atualizar: ")

            if not self.existe(id_livro):
                print(" Livro não encontrado!")
                return

            conn = self.mysql.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM livro WHERE id_livro = %s", (id_livro,))
            livro_atual = cursor.fetchone()

            print("\n===== DADOS ATUAIS DO LIVRO =====")
            for campo, valor in livro_atual.items():
                print(f"{campo}: {valor}")
            print("=================================\n")

            print("Deixe o campo em branco para manter o valor atual.\n")

            genero = input(f"Novo gênero [{livro_atual['genero']}]: ") or livro_atual['genero']
            titulo = input(f"Novo título [{livro_atual['titulo']}]: ") or livro_atual['titulo']
            autor = input(f"Novo autor [{livro_atual['autor']}]: ") or livro_atual['autor']
            editora = input(f"Nova editora [{livro_atual['editora']}]: ") or livro_atual['editora']
            ano_publicacao = input(f"Novo ano de publicação [{livro_atual['ano_publicacao']}]: ") or livro_atual['ano_publicacao']
            localizacao = input(f"Nova localização [{livro_atual['localizacao']}]: ") or livro_atual['localizacao']
            num_paginas = input(f"Novo número de páginas [{livro_atual['num_paginas']}]: ") or livro_atual['num_paginas']
            estoque = input(f"Novo estoque [{livro_atual['estoque']}]: ") or livro_atual['estoque']
            disponivel_input = input(f"Disponível (S/N) [{ 'S' if livro_atual['disponivel'] else 'N' }]: ").strip().upper()

            disponivel = livro_atual['disponivel']
            if disponivel_input == "S":
                disponivel = 1
            elif disponivel_input == "N":
                disponivel = 0

            sql = """
                UPDATE livro SET
                    genero = %s,
                    titulo = %s,
                    autor = %s,
                    editora = %s,
                    ano_publicacao = %s,
                    localizacao = %s,
                    num_paginas = %s,
                    estoque = %s,
                    disponivel = %s
                WHERE id_livro = %s
            """
            valores = (
                genero, titulo, autor, editora, ano_publicacao,
                localizacao, num_paginas, estoque, disponivel, id_livro
            )

            cursor.execute(sql, valores)
            conn.commit()
            print("\n Livro atualizado com sucesso!")

        except mysql.connector.Error as err:
            print(f" Erro ao atualizar livro: {err}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ---------------- DELETAR LIVRO ----------------
    def deletar(self, id_livro):
        conn = None
        cursor = None
        try:
            if not self.existe(id_livro):
                print(" Livro não encontrado!")
                return

            conn = self.mysql.connect()
            cursor = conn.cursor()

            # 🔍 Verifica se o livro está em algum empréstimo
            cursor.execute("SELECT COUNT(*) FROM emprestimo WHERE id_livro = %s", (id_livro,))
            emprestimos = cursor.fetchone()[0]

            if emprestimos > 0:
                print(f" O livro com ID {id_livro} possui {emprestimos} empréstimo(s) registrado(s).")
                print(" Exclusão não permitida para manter o histórico de empréstimos.")
                return

            cursor.execute("DELETE FROM livro WHERE id_livro = %s", (id_livro,))
            conn.commit()

            if cursor.rowcount > 0:
                print(" Livro deletado com sucesso!")
            else:
                print(" Nenhum livro encontrado com esse ID.")
        except mysql.connector.Error as err:
            print(f" Erro ao deletar livro: {err}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ---------------- BUSCAR POR ID ----------------
    def buscar_por_id(self, id_livro):
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livro WHERE id_livro = %s", (id_livro,))
            result = cursor.fetchone()
            if result:
                print("📘 Livro encontrado!")
                return Livro(*result)
            print(" Nenhum livro encontrado com esse ID.")
            return None
        except mysql.connector.Error as err:
            print(f" Erro ao buscar livro: {err}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ---------------- ATUALIZAR DISPONIBILIDADE ----------------
    def atualizar_disponibilidade(self, id_livro, disponivel):
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE livro SET disponivel = %s WHERE id_livro = %s",
                (int(disponivel), id_livro)
            )
            conn.commit()
            print(f" Disponibilidade do livro {id_livro} atualizada para {bool(disponivel)}.")
        except mysql.connector.Error as err:
            print(f" Erro ao atualizar disponibilidade do livro: {err}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ---------------- VERIFICAR EXISTÊNCIA ----------------
    def existe(self, id_livro):
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM livro WHERE id_livro = %s", (id_livro,))
            qtd = cursor.fetchone()[0]
            return qtd > 0
        except mysql.connector.Error as err:
            print(f" Erro ao verificar existência do livro: {err}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
