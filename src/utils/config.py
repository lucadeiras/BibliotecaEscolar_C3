MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Alunos
2 - Relatório de Livros
3 - Relatório de Empréstimos
0 - Voltar
"""

MENU_ENTIDADES = """Entidades
1 - ALUNO
2 - LIVRO
3 - EMPRÉSTIMO
0 - Voltar
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time: int = 3):
    """
    Limpa a tela após alguns segundos.
    wait_time: tempo de espera em segundos.
    """
    import os
    from time import sleep
    sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")
