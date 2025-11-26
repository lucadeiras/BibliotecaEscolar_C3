
# Main menu for BibliotecaEscolar C3
from src.utils.splash_screen import show
from pymongo import MongoClient
import importlib
import pkgutil
import sys

def menu():
    print('\nMenu principal:')
    print('1 - Relatorios')
    print('2 - Inserir documentos')
    print('3 - Remover documentos')
    print('4 - Atualizar documentos')
    print('5 - Sair')

def run():
    show()
    client = MongoClient('mongodb://localhost:27017')
    db = client['biblioteca']
    while True:
        menu()
        op = input('Escolha uma opcao: ').strip()
        if op == '1':
            from src.reports import relatorios
            relatorios.main()
        elif op == '2':
            print('Inserir documentos - use create_collections_and_data.py ou implemente insercao manual no projeto.')
        elif op == '3':
            print('Remover documentos - ainda nao implementado via menu. Use o script ou Mongo shell.')
        elif op == '4':
            print('Atualizar documentos - ainda nao implementado via menu. Use o script ou Mongo shell.')
        elif op == '5':
            print('Saindo...')
            break
        else:
            print('Opcao invalida.')

if __name__ == '__main__':
    run()
