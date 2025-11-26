# src/controller/controller_emprestimo.py
import mysql.connector
from src.model.emprestimo import Emprestimo
from src.model.aluno import Aluno
from src.model.livro import Livro
from src.conexion.mySQL_queries import mySQL_queries


class ControllerEmprestimo:
    def __init__(self):
        self.mysql = mySQL_queries()
        

    def registrar_emprestimo(self, emprestimo: Emprestimo):
        """Registra um novo empréstimo no banco de dados."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()

            # 🔍 Verifica se o aluno existe
            cursor.execute(
                "SELECT COUNT(*) FROM aluno WHERE matricula = %s",
                (emprestimo.get_aluno().get_matricula(),)
            )
            if cursor.fetchone()[0] == 0:
                print("❌ Erro: matrícula não encontrada no banco de dados.")
                return

            # 🔍 Verifica se o livro existe e está disponível
            cursor.execute(
                "SELECT disponivel FROM livro WHERE id_livro = %s",
                (emprestimo.get_livro().get_id_livro(),)
            )
            result = cursor.fetchone()
            if not result:
                print("❌ Erro: livro não encontrado.")
                return
            elif result[0] == 0:
                print("⚠️ O livro selecionado está indisponível para empréstimo.")
                return

            # 💾 Insere o empréstimo
            sql = """
                INSERT INTO emprestimo (
                    matricula, id_livro, data_emprestimo,
                    data_devolucao, atraso, multa, emprestado
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                emprestimo.get_aluno().get_matricula(),
                emprestimo.get_livro().get_id_livro(),
                emprestimo.get_data_emprestimo(),
                emprestimo.get_data_devolucao(),
                int(emprestimo.get_atraso()),
                emprestimo.get_multa(),
                int(emprestimo.get_emprestado())
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("✅ Empréstimo registrado com sucesso!")

            # 📚 Atualiza disponibilidade do livro
            cursor.execute(
                "UPDATE livro SET disponivel = 0 WHERE id_livro = %s",
                (emprestimo.get_livro().get_id_livro(),)
            )
            conn.commit()
            print("📘 Livro marcado como indisponível.")
        except mysql.connector.Error as err:
            print(f"❌ Erro ao registrar empréstimo: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def finalizar_emprestimo(self, id_emprestimo):
        """Finaliza um empréstimo e torna o livro disponível novamente."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()

            # Recupera o ID do livro do empréstimo
            cursor.execute(
                "SELECT id_livro FROM emprestimo WHERE id_emprestimo = %s",
                (id_emprestimo,)
            )
            result = cursor.fetchone()
            if result:
                id_livro = result[0]
                cursor.execute(
                    "UPDATE livro SET disponivel = 1 WHERE id_livro = %s",
                    (id_livro,)
                )
                print("📖 Livro devolvido e marcado como disponível.")

            # Atualiza status do empréstimo
            cursor.execute(
                "UPDATE emprestimo SET emprestado = 0 WHERE id_emprestimo = %s",
                (id_emprestimo,)
            )
            conn.commit()
            print("✅ Empréstimo finalizado com sucesso!")
        except mysql.connector.Error as err:
            print(f"❌ Erro ao finalizar empréstimo: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def listar_todos(self):
        """Retorna uma lista com todos os empréstimos registrados."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM emprestimo")
            result = cursor.fetchall()
            print("📋 Lista de empréstimos carregada com sucesso.")
            return result
        except mysql.connector.Error as err:
            print(f"❌ Erro ao listar empréstimos: {err}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def existe(self, id_emprestimo):
        """Verifica se um empréstimo existe no banco."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM emprestimo WHERE id_emprestimo = %s",
                (id_emprestimo,)
            )
            qtd = cursor.fetchone()[0]
            return qtd > 0
        except mysql.connector.Error as err:
            print(f"❌ Erro ao verificar existência do empréstimo: {err}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def deletar(self, id_emprestimo=None):
        """
        Deleta um empréstimo do banco.
        Pode ser chamado diretamente com ID (deletar(5))
        ou de forma interativa (sem parâmetros).
        """
        conn = None
        cursor = None
        try:
            if id_emprestimo is None:
                id_emprestimo = input("Informe o ID do empréstimo a ser removido: ")

            conn = self.mysql.connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM emprestimo WHERE id_emprestimo = %s",
                (id_emprestimo,)
            )
            if cursor.fetchone()[0] == 0:
                print("⚠️ Empréstimo não encontrado.")
                return

            confirm = input(f"Confirma exclusão do empréstimo {id_emprestimo}? [s/N]: ").strip().lower()
            if confirm != "s":
                print("Exclusão cancelada.")
                return
            cursor.execute("DELETE FROM emprestimo WHERE id_emprestimo = %s", (id_emprestimo,))
            conn.commit()
            print(f"✅ Empréstimo {id_emprestimo} removido com sucesso!")
        except mysql.connector.Error as err:
            print(f"❌ Erro ao remover empréstimo: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()