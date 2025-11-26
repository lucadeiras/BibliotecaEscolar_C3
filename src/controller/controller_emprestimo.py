from src.db.connection import get_db
from datetime import datetime

def listar(db):
    coll = db['emprestimos']
    docs = list(coll.find({}))
    if not docs:
        print('Nenhum empréstimo cadastrado.')
        return []
    print('\n--- Lista de empréstimos ---')
    for i, d in enumerate(docs, start=1):
        print(f"{i}) _id={d.get('_id')} | aluno_id={d.get('aluno_id')} livro_id={d.get('livro_id')} data_inicio={d.get('data_inicio')} devolucao={d.get('data_devolucao')}")
    return docs

def inserir(db):
    print('\n--- Inserir empréstimo ---')
    # escolha aluno
    from src.controllers.aluno_controller import listar as listar_alunos
    alunos = listar_alunos(db)
    if not alunos:
        print('Cadastre alunos antes.')
        return
    a = input('Escolha o número do aluno: ').strip()
    try:
        aluno = alunos[int(a)-1]
    except:
        print('Escolha inválida.')
        return
    # escolha livro
    from src.controllers.livro_controller import listar as listar_livros
    livros = listar_livros(db)
    if not livros:
        print('Cadastre livros antes.')
        return
    l = input('Escolha o número do livro: ').strip()
    try:
        livro = livros[int(l)-1]
    except:
        print('Escolha inválida.')
        return
    data_inicio = input('Data de início (YYYY-mm-dd) [hoje]: ').strip()
    if not data_inicio:
        data_inicio = datetime.now()
    else:
        try:
            data_inicio = datetime.fromisoformat(data_inicio)
        except:
            print('Formato inválido, usando hoje.')
            data_inicio = datetime.now()
    doc = {'aluno_id': aluno.get('_id'), 'livro_id': livro.get('_id'), 'data_inicio': data_inicio, 'data_devolucao': None}
    res = db['emprestimos'].insert_one(doc)
    print('Empréstimo criado com _id=', res.inserted_id)

def escolher(db):
    docs = listar(db)
    if not docs:
        return None
    escolha = input('Escolha o número do registro: ').strip()
    try:
        idx = int(escolha)-1
        if idx < 0 or idx >= len(docs):
            print('Escolha inválida.')
            return None
        return docs[idx]
    except:
        print('Entrada inválida.')
        return None

def atualizar(db):
    print('\n--- Atualizar empréstimo (registrar devolução) ---')
    doc = escolher(db)
    if not doc:
        return
    print('Registro selecionado:', doc)
    devol = input('Registrar data de devolução (YYYY-mm-dd) [hoje]: ').strip()
    if not devol:
        devol = datetime.now()
    else:
        try:
            devol = datetime.fromisoformat(devol)
        except:
            print('Formato inválido, usando hoje.')
            devol = datetime.now()
    db['emprestimos'].update_one({'_id': doc.get('_id')}, {'$set': {'data_devolucao': devol}})
    print('Devolução registrada.')

def remover(db):
    print('\n--- Remover empréstimo ---')
    doc = escolher(db)
    if not doc:
        return
    confirma = input('Confirmar remoção deste empréstimo? (s/N): ').strip().lower()
    if confirma != 's':
        print('Cancelado.')
        return
    db['emprestimos'].delete_one({'_id': doc.get('_id')})
    print('Empréstimo removido.')

if __name__ == '__main__':
    db = get_db()
    while True:
        print('\nEmprestimos: 1-listar 2-inserir 3-atualizar 4-remover 0-sair')
        op = input('Op: ').strip()
        if op == '1': listar(db)
        elif op == '2': inserir(db)
        elif op == '3': atualizar(db)
        elif op == '4': remover(db)
        elif op == '0': break
        else: print('inválido')

