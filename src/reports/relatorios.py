
# Reports for BibliotecaEscolar C3
# Two reports:
# 1) Aggregation: number of emprestimos per aluno (group)
# 2) Join-like report: emprestimos with aluno and livro details (lookup)
from pymongo import MongoClient
import argparse
def rel_agrupamento(db):
    pipeline = [
        {'$group': {'_id': '$aluno_id', 'total_emprestimos': {'$sum': 1}}},
        {'$sort': {'total_emprestimos': -1}}
    ]
    print('--- Emprestimos por aluno ---')
    for doc in db['emprestimos'].aggregate(pipeline):
        print(doc)

def rel_join(db):
    pipeline = [
        {'$lookup': {
            'from': 'alunos',
            'localField': 'aluno_id',
            'foreignField': '_id',
            'as': 'aluno'
        }},
        {'$lookup': {
            'from': 'livros',
            'localField': 'livro_id',
            'foreignField': '_id',
            'as': 'livro'
        }},
        {'$unwind': '$aluno'},
        {'$unwind': '$livro'},
        {'$project': {
            '_id':1, 'data_inicio':1, 'aluno.nome':1, 'livro.titulo':1
        }}
    ]
    print('--- Emprestimos com detalhes (join) ---')
    for doc in db['emprestimos'].aggregate(pipeline):
        print(doc)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--uri', default='mongodb://localhost:27017')
    parser.add_argument('--db', default='biblioteca')
    args = parser.parse_args()
    client = MongoClient(args.uri)
    db = client[args.db]
    rel_agrupamento(db)
    rel_join(db)

if __name__ == '__main__':
    main()
