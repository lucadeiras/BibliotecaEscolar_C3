from src.db.connection import get_db

def listar(db):
    coll = db['alunos']
    docs = list(coll.find({}))
    if not docs:
        print('Nenhum aluno cadastrado.')
        return []
    print('\n--- Lista de alunos ---')
    for i, d in enumerate(docs, start=1):
        print(f"{i}) _id={d.get('_id')} | {d.get('nome')} - {d.get('curso')} matricula:{d.get('matricula')}")
    return docs

def inserir(db):
    print('\n--- Inserir aluno ---')
    nome = input('Nome: ').strip()
    curso = input('Curso: ').strip()
    matricula = input('Matrícula: ').strip()
    doc = {'nome': nome, 'curso': curso, 'matricula': matricula}
    res = db['alunos'].insert_one(doc)
    print('Aluno inserido com _id =', res.inserted_id)

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
    print('\n--- Atualizar aluno ---')
    doc = escolher(db)
    if not doc:
        return
    nome = input(f'Nome [{doc.get("nome")}]: ').strip() or doc.get('nome')
    curso = input(f'Curso [{doc.get("curso")}]: ').strip() or doc.get('curso')
    matricula = input(f'Matrícula [{doc.get("matricula")}]: ').strip() or doc.get('matricula')
    db['alunos'].update_one({'_id': doc.get('_id')}, {'$set': {'nome': nome, 'curso': curso, 'matricula': matricula}})
    print('Aluno atualizado.')

def remover(db):
    print('\n--- Remover aluno ---')
    doc = escolher(db)
    if not doc:
        return
    emprestimos = list(db['emprestimos'].find({'aluno_id': doc.get('_id')}))
    if emprestimos:
        print('Este aluno possui empréstimos associados.')
        confirma = input('Deseja remover o aluno e os empréstimos relacionados? (s/N): ').strip().lower()
        if confirma != 's':
            print('Operação cancelada.')
            return
        db['emprestimos'].delete_many({'aluno_id': doc.get('_id')})
        print('Empréstimos relacionados removidos.')
    db['alunos'].delete_one({'_id': doc.get('_id')})
    print('Aluno removido.')

if __name__ == '__main__':
    db = get_db()
    while True:
        print('\nAlunos: 1-listar 2-inserir 3-atualizar 4-remover 0-sair')
        op = input('Op: ').strip()
        if op == '1': listar(db)
        elif op == '2': inserir(db)
        elif op == '3': atualizar(db)
        elif op == '4': remover(db)
        elif op == '0': break
        else: print('inválido')
