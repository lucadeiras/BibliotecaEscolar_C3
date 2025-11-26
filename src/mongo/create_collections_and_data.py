
# Script to create MongoDB collections and insert sample data for the BibliotecaEscolar project (C3)
# Usage (Linux): Ensure MongoDB is running and `pymongo` is installed:
#   pip install pymongo
#   python3 create_collections_and_data.py --uri mongodb://localhost:27017 --db biblioteca
import argparse
from pymongo import MongoClient
import datetime
import json

def create_data(db):
    # Collections: livros, alunos (example two collections with relation: emprestimos references alunos and livros)
    db.drop_collection('livros')
    db.drop_collection('alunos')
    db.drop_collection('emprestimos')

    livros = [
        {'_id': 1, 'titulo': 'Aprendendo Java', 'autor': 'Fulano', 'ano': 2019, 'quantidade': 3},
        {'_id': 2, 'titulo': 'Algoritmos e Estruturas', 'autor': 'Ciclano', 'ano': 2018, 'quantidade': 2},
    ]
    alunos = [
        {'_id': 101, 'nome': 'Aluno Um', 'curso': 'CC', 'matricula': '20201234'},
        {'_id': 102, 'nome': 'Aluno Dois', 'curso': 'SI', 'matricula': '20205678'},
    ]
    emprestimos = [
        {'_id': 1001, 'aluno_id': 101, 'livro_id': 1, 'data_inicio': datetime.datetime(2025,1,10), 'data_devolucao': None},
        {'_id': 1002, 'aluno_id': 102, 'livro_id': 2, 'data_inicio': datetime.datetime(2025,2,12), 'data_devolucao': None},
    ]
    db['livros'].insert_many(livros)
    db['alunos'].insert_many(alunos)
    db['emprestimos'].insert_many(emprestimos)
    print('Collections created and sample data inserted.')

def main():
    parser = argparse.ArgumentParser(description='Create MongoDB collections and sample data for BibliotecaEscolar C3')
    parser.add_argument('--uri', default='mongodb://localhost:27017', help='MongoDB URI')
    parser.add_argument('--db', default='biblioteca', help='Database name')
    args = parser.parse_args()

    client = MongoClient(args.uri)
    db = client[args.db]
    create_data(db)
    # show counts
    for c in ['livros','alunos','emprestimos']:
        print(c, db[c].count_documents({}))

if __name__ == '__main__':
    main()
