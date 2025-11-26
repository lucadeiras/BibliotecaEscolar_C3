
from src.utils.splash_screen import show
from src.db.connection import get_db
import sys

def menu_principal():
    print('\nMenu principal:')
    print('1 - Relatorios')
    print('2 - Livros (CRUD)')
    print('3 - Alunos (CRUD)')
    print('4 - Emprestimos (CRUD)')
    print('5 - Sair')

def menu_crud(nome):
    print(f'\n{nome} - Escolha ação:')
    print('1 - Listar')
    print('2 - Inserir')
    print('3 - Atualizar')
    print('4 - Remover')
    print('0 - Voltar')

def run():
    show()
    db = get_db()
    while True:
        menu_principal()
        op = input('Escolha uma opcao: ').strip()
        if op == '1':
            from src.reports import relatorios
            relatorios.main()
        elif op == '2':
            from src.controllers import livro_controller as ctrl
            while True:
                menu_crud('Livros')
                o = input('Op: ').strip()
                if o == '1': ctrl.listar(db)
                elif o == '2': ctrl.inserir(db)
                elif o == '3': ctrl.atualizar(db)
                elif o == '4': ctrl.remover(db)
                elif o == '0': break
                else: print('Opcao invalida')
        elif op == '3':
            from src.controllers import aluno_controller as ctrl
            while True:
                menu_crud('Alunos')
                o = input('Op: ').strip()
                if o == '1': ctrl.listar(db)
                elif o == '2': ctrl.inserir(db)
                elif o == '3': ctrl.atualizar(db)
                elif o == '4': ctrl.remover(db)
                elif o == '0': break
                else: print('Opcao invalida')
        elif op == '4':
            from src.controllers import emprestimo_controller as ctrl
            while True:
                menu_crud('Emprestimos')
                o = input('Op: ').strip()
                if o == '1': ctrl.listar(db)
                elif o == '2': ctrl.inserir(db)
                elif o == '3': ctrl.atualizar(db)
                elif o == '4': ctrl.remover(db)
                elif o == '0': break
                else: print('Opcao invalida')
        elif op == '5':
            print('Saindo...')
            sys.exit(0)
        else:
            print('Opcao invalida')

if __name__ == '__main__':
    run()
