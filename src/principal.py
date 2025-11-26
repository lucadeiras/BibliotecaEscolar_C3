from src.utils import config
from src.model.livro import Livro
from src.model.aluno import Aluno
from src.model.emprestimo import Emprestimo
from src.utils.splash_screen import SplashScreen
from src.reports.relatorios import Relatorios
from src.controller.controller_aluno import ControllerAluno
from src.controller.controller_livro import ControllerLivro
from src.controller.controller_emprestimo import ControllerEmprestimo
from src.conexion.mySQL_queries import mySQL_queries
from datetime import datetime
import mysql.connector

# Instâncias principais
tela_inicial = SplashScreen()
relatorio = Relatorios()
ctrl_aluno = ControllerAluno()
ctrl_livro = ControllerLivro()
ctrl_emprestimo = ControllerEmprestimo()

# ---------------- RELATÓRIOS ----------------
def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_alunos(mostrar_pause=True)
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_livros(mostrar_pause=True)
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_emprestimos(mostrar_pause=True)

# ---------------- INSERIR ----------------
def inserir():
    while True:
        print(config.MENU_ENTIDADES)
        opcao_inserir = int(input("Escolha uma opção [0-3]: "))
        config.clear_console(1)

        if opcao_inserir == 0:
            config.clear_console()
            return

        elif opcao_inserir == 1:
            print("\n--- Inserção de Aluno ---")
            matricula = input("Matrícula: ")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            turma = input("Turma: ")
            data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")

            aluno = {
                "Matricula": matricula,
                "Nome": nome,
                "CPF": cpf,
                "Email": email,
                "Telefone": telefone,
                "Endereco": endereco,
                "Turma": turma,
                "Data_Nascimento": data_nascimento
            }

            ctrl_aluno.inserir(aluno)

        elif opcao_inserir == 2:
            print("\n--- Inserção de Livro ---")
            genero = input("Gênero: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            editora = input("Editora: ")
            ano_publicacao = input("Ano de Publicação: ")
            localizacao = input("Localização: ")
            num_paginas = input("Número de Páginas: ")
            estoque = input("Estoque: ")
            disponivel = input("Disponível (S/N): ").strip().upper() == "S"

            livro = Livro(
                id_livro=None,
                genero=genero,
                titulo=titulo,
                autor=autor,
                editora=editora,
                ano_publicacao=ano_publicacao,
                localizacao=localizacao,
                num_paginas=num_paginas,
                estoque=estoque,
                disponivel=disponivel
            )

            ctrl_livro.inserir(livro)

        elif opcao_inserir == 3:
            print("\n--- Registro de Empréstimo ---")

            matricula = input("Matrícula do aluno: ")
            titulo_livro = input("Título do livro: ")
            data_emprestimo = input("Data do empréstimo (AAAA-MM-DD): ")
            data_devolucao = input("Data prevista de devolução (AAAA-MM-DD): ")

            # Correção: conexão segura e compatível com Linux
            mysql = mySQL_queries()
            conn = None
            cursor = None
            try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT id_livro FROM livro WHERE titulo = %s", (titulo_livro,))
                result = cursor.fetchone()

                if not result:
                    print(f"❌ Livro '{titulo_livro}' não encontrado!")
                    return

                id_livro = result[0]

                aluno = Aluno(matricula, None, None, None, None, None, None, None)
                livro = Livro(id_livro, None, titulo_livro, None, None, None, None, None, None, True)

                emprestimo = Emprestimo(
                    id_emprestimo=None,
                    aluno=aluno,
                    livro=livro,
                    data_emprestimo=data_emprestimo,
                    data_devolucao=data_devolucao,
                    atraso=False,
                    multa=0.0,
                    emprestado=True
                )

                ctrl_emprestimo.registrar_emprestimo(emprestimo)
            except Exception as e:
                print(f"❌ Erro ao registrar empréstimo: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    mysql.close()

# ---------------- ATUALIZAR ----------------
def atualizar():
    while True:
        print(config.MENU_ENTIDADES)
        opcao_atualizar = int(input("Escolha uma opção [0-3]: "))
        config.clear_console(1)

        if opcao_atualizar == 0:
            return

        elif opcao_atualizar == 1:
            print("\n===== RELATÓRIO DE ALUNOS =====")
            relatorio.get_relatorio_alunos(mostrar_pause=False)
            ctrl_aluno.atualizar()

        elif opcao_atualizar == 2:
            print("\n===== RELATÓRIO DE LIVROS =====")
            relatorio.get_relatorio_livros(mostrar_pause=False)
            ctrl_livro.atualizar()

        elif opcao_atualizar == 3:
            print("\n===== RELATÓRIO DE EMPRÉSTIMOS =====")
            relatorio.get_relatorio_emprestimos(mostrar_pause=False)
            id_emprestimo = input("Informe o ID do empréstimo a finalizar: ")
            ctrl_emprestimo.finalizar_emprestimo(id_emprestimo)

# ---------------- EXCLUIR ----------------
def excluir():
    while True:
        print(config.MENU_ENTIDADES)
        opcao_excluir = int(input("Escolha uma opção [0-3]: "))
        config.clear_console(1)

        if opcao_excluir == 0:
            return

        elif opcao_excluir == 1:
            print("\n===== RELATÓRIO DE ALUNOS =====")
            relatorio.get_relatorio_alunos(mostrar_pause=False)
            matricula = input("Informe a matrícula do aluno a ser removido: ")
            ctrl_aluno.deletar(matricula)

        elif opcao_excluir == 2:
            print("\n===== RELATÓRIO DE LIVROS =====")
            relatorio.get_relatorio_livros(mostrar_pause=False)
            id_livro = input("Informe o ID do livro a ser removido: ")
            ctrl_livro.deletar(id_livro)

        elif opcao_excluir == 3:
            print("\n===== RELATÓRIO DE EMPRÉSTIMOS =====")
            relatorio.get_relatorio_emprestimos(mostrar_pause=False)
            id_emprestimo = input("Informe o ID do empréstimo a ser removido (use com cautela): ")
            ctrl_emprestimo.deletar(id_emprestimo)

# ---------------- EXECUÇÃO PRINCIPAL ----------------
def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1:
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-3]: "))
            if opcao_relatorio == 0:
                config.clear_console()
                continue
            reports(opcao_relatorio)
            config.clear_console()

        elif opcao == 2:
            inserir()

        elif opcao == 3:
            atualizar()

        elif opcao == 4:
            excluir()

        elif opcao == 5:
            config.clear_console()
            print("Obrigado por utilizar o sistema da biblioteca.")
            exit(0)

        else:
            print("Opção incorreta.")
            config.clear_console(1)

if __name__ == "__main__":
    run()
