from src.db.connection import get_db
from src.controllers.helpers import parse_id

def listar(db):
    coll = db['livros']
    docs = list(coll.find({}))
    if not docs:
        print('Nenhum livro cadastrado.')
        return []
    print('\n--- Lista de livros ---')
    for i, d in enumerate(docs, start=1):
        print(f"{i}) _id={d.get('_id')} | {d.get('titulo')} - {d.get('autor')} ({d.get('ano')}) qtd:{d.get('quantidade')}")
    return docs

def inserir(db):
    print('\n--- Inserir livro ---')
    titulo = input('Título: ').strip()
    autor = input('Autor: ').strip()
    ano = input('Ano (opcional): ').strip() or None
    qtd = input('Quantidade: ').strip() or '1'
    try:
        ano = int(ano) if ano else None
    except:
        ano = None
    try:
        qtd = int(qtd)
    except:
        qtd = 1
    doc = {'titulo': titulo, 'autor': autor, 'ano': ano, 'quantidade': qtd}
    coll = db['livros']
    res = coll.insert_one(doc)
    print('Livro inserido com _id =', res.inserted_id)

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
    print('\n--- Atualizar livro ---')
    doc = escolher(db)
    if not doc:
        return
    print('Registro selecionado:', doc)
    titulo = input(f'Título [{doc.get("titulo")}]: ').strip() or doc.get('titulo')
    autor = input(f'Autor [{doc.get("autor")}]: ').strip() or doc.get('autor')
    ano = input(f'Ano [{doc.get("ano")}]: ').strip() or doc.get('ano')
    qtd = input(f'Quantidade [{doc.get("quantidade")}]: ').strip() or doc.get('quantidade')
    try:
        ano = int(ano) if ano not in (None, '') else None
    except:
        ano = doc.get('ano')
    try:
        qtd = int(qtd)
    except:
        qtd = doc.get('quantidade')
    filtro = {'_id': doc.get('_id')}
    novos = {'$set': {'titulo': titulo, 'autor': autor, 'ano': ano, 'quantidade': qtd}}
    db['livros'].update_one(filtro, novos)
    print('Atualizado.')

def remover(db):
    print('\n--- Remover livro ---')
    doc = escolher(db)
    if not doc:
        return
    # verificar referências em emprestimos
    emprestimos = list(db['emprestimos'].find({'livro_id': doc.get('_id')}))
    if emprestimos:
        print('Este livro possui empréstimos associados (não pode ser removido sem confirmar).')
        confirma = input('Deseja remover o livro e os empréstimos relacionados? (s/N): ').strip().lower()
        if confirma != 's':
            print('Operação cancelada.')
            return
        # remover emprestimos relacionados
        db['emprestimos'].delete_many({'livro_id': doc.get('_id')})
        print('Empréstimos relacionados removidos.')
    db['livros'].delete_one({'_id': doc.get('_id')})
    print('Livro removido.')

if __name__ == '__main__':
    db = get_db()
    while True:
        print('\nLivros: 1-listar 2-inserir 3-atualizar 4-remover 0-sair')
        op = input('Op: ').strip()
        if op == '1': listar(db)
        elif op == '2': inserir(db)
        elif op == '3': atualizar(db)
        elif op == '4': remover(db)
        elif op == '0': break
        else: print('inválido')
