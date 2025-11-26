
# Splash screen utility for BibliotecaEscolar C3
from pymongo import MongoClient
import datetime
def show(uri='mongodb://localhost:27017', dbname='biblioteca'):
    client = MongoClient(uri)
    db = client[dbname]
    counts = {c: db[c].count_documents({}) for c in ['livros','alunos','emprestimos'] if c in db.list_collection_names()}
    print('===================================================')
    print('Sistema: Biblioteca Escolar - C3 (Trabalho de BD NoSQL)')
    print('Componentes do grupo: <Coloque os nomes aqui>')
    print('Professor: Howard Roatti')
    print('Disciplina: Banco de Dados')
    print('Data:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('Contagem de documentos por coleção:')
    for k,v in counts.items():
        print(f'  {k}: {v}')
    print('===================================================')
