# src/controller/controller_aluno.py
from src.conexion.mySQL_queries import mySQL_queries


class ControllerAluno:
    def __init__(self):
        # não abre a conexão aqui para evitar conexões abertas por muito tempo
        self.mysql = mySQL_queries()

    def existe(self, matricula):
        """Verifica se existe aluno com a matrícula (retorna bool)."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM aluno WHERE Matricula = %s", (matricula,))
            qtd = cursor.fetchone()[0]
            return qtd > 0
        except Exception as e:
            print(f"❌ Erro ao verificar existência do aluno: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            try:
                self.mysql.close()
            except Exception:
                pass

    def inserir(self, aluno: dict):
        """
        Insere um aluno no banco a partir de um dicionário com chaves:
        Matricula, Nome, CPF, Email, Telefone, Endereco, Turma, Data_Nascimento
        """
        conn = None
        cursor = None
        try:
            if "Matricula" not in aluno or "Nome" not in aluno:
                print("⚠️ Dados incompletos do aluno. Matricula e Nome são obrigatórios.")
                return

            conn = self.mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(1) FROM aluno WHERE Matricula = %s", (aluno["Matricula"],))
            if cursor.fetchone()[0] > 0:
                print(f"⚠️ Já existe um aluno com a matrícula {aluno['Matricula']}.")
                return

            sql = """
                INSERT INTO aluno
                (Matricula, Nome, CPF, Email, Telefone, Endereco, Turma, Data_Nascimento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                aluno.get("Matricula"),
                aluno.get("Nome"),
                aluno.get("CPF", None),
                aluno.get("Email", None),
                aluno.get("Telefone", None),
                aluno.get("Endereco", None),
                aluno.get("Turma", None),
                aluno.get("Data_Nascimento", None)
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("✅ Aluno inserido com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao inserir aluno: {e}")
        finally:
            if cursor:
                cursor.close()
            try:
                self.mysql.close()
            except Exception:
                pass

    def atualizar(self):
        """Interativo: atualiza email/telefone/endereço de um aluno."""
        matricula = input("Informe a matrícula do aluno que deseja atualizar: ")
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM aluno WHERE Matricula = %s", (matricula,))
            if cursor.fetchone()[0] == 0:
                print("⚠️ Aluno não encontrado.")
                return

            novo_email = input("Novo email (enter para manter): ").strip()
            novo_telefone = input("Novo telefone (enter para manter): ").strip()
            novo_endereco = input("Novo endereço (enter para manter): ").strip()

            campos = []
            valores = []
            if novo_email:
                campos.append("Email = %s")
                valores.append(novo_email)
            if novo_telefone:
                campos.append("Telefone = %s")
                valores.append(novo_telefone)
            if novo_endereco:
                campos.append("Endereco = %s")
                valores.append(novo_endereco)

            if not campos:
                print("Nada para atualizar.")
                return

            sql = "UPDATE aluno SET " + ", ".join(campos) + " WHERE Matricula = %s"
            valores.append(matricula)
            cursor.execute(sql, tuple(valores))
            conn.commit()
            print("✅ Dados do aluno atualizados com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao atualizar aluno: {e}")
        finally:
            if cursor:
                cursor.close()
            try:
                self.mysql.close()
            except Exception:
                pass

    def deletar(self, matricula):
        """Deleta um aluno pela matrícula (usado pelo principal.py)."""
        conn = None
        cursor = None
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM aluno WHERE Matricula = %s", (matricula,))
            if cursor.fetchone()[0] == 0:
                print("⚠️ Aluno não encontrado.")
                return

            confirm = input(f"Confirma exclusão do aluno {matricula}? [s/N]: ").strip().lower()
            if confirm in ("s", "sim", "y", "yes"):
                cursor.execute("DELETE FROM aluno WHERE Matricula = %s", (matricula,))
                conn.commit()
                print("✅ Aluno removido com sucesso!")
            else:
                print("Exclusão cancelada.")
                return

        
        except Exception as e:
            print(f"❌ Erro ao remover aluno: {e}")
        finally:
            if cursor:
                cursor.close()
            try:
                self.mysql.close()
            except Exception:
                pass
