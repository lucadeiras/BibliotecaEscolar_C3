
# BibliotecaEscolar - C3 (Entrega para Banco de Dados - MongoDB)
Este projeto adapta o trabalho da C2 para o edital C3, usando MongoDB.

## O que foi incluído
- `src/mongo/create_collections_and_data.py` : cria coleções `livros`, `alunos`, `emprestimos` e insere dados de exemplo.
- `src/reports/relatorios.py` : dois relatórios (agregação e join via $lookup).
- `src/utils/splash_screen.py` : exibe splash com contagem de documentos e nomes do grupo (substitua pelos nomes reais).
- `src/main_c3.py` : menu inicial (console) que chama os relatórios e scripts.
- `C3_INSPECTION.txt` : listagem dos arquivos originais (inspeção do projeto C2).
- `diagram_relacional.pdf` : placeholder (substitua pelo diagrama real gerado pelo SQL Power Architect).

## Como executar (Linux)
1. Tenha o MongoDB rodando localmente (padrão: `mongodb://localhost:27017`).
2. Instale dependências:
   ```
   pip install pymongo
   ```
3. Criar coleções e dados de exemplo:
   ```
   python3 src/mongo/create_collections_and_data.py --uri mongodb://localhost:27017 --db biblioteca
   ```
4. Executar menu principal:
   ```
   python3 -m src.main_c3
   ```
5. Rodar relatórios diretamente:
   ```
   python3 src/reports/relatorios.py
   ```

## Observações
- Substitua `<Coloque os nomes aqui>` no splash por nomes reais dos membros do grupo.
- Complete as funções de inserção, remoção e atualização pelo menu conforme necessário (o esqueleto foi preparado).
- Gere o diagrama relacional com o SQL Power Architect e substitua `diagram_relacional.pdf`.
