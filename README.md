# Sistema de Gerenciamento de Biblioteca Escolar em Python com MySQL (Aiven)

Esse sistema foi desenvolvido em **Python** para o gerenciamento de **alunos, livros e empréstimos** de uma biblioteca escolar.  
O sistema utiliza um banco de dados **MySQL** hospedado na nuvem através da plataforma **Aiven**.

O sistema exige que as tabelas existam previamente no banco de dados.  
Para isso, basta executar o script Python a seguir para **criação das tabelas** e **inserção de registros iniciais**:

```shell
~$ python src/create_tables_and_records.py
```

Após a criação das tabelas, o sistema pode ser executado com o seguinte comando:

```shell
~$ python src/principal.py
```

Para testar a conexão com o banco de dados MySQL (Aiven) e o módulo de conexão desenvolvido, execute:

```shell
~$ python src/test.py
```

---

## Organização

- [diagrams](diagrams): Nesse diretório encontra-se o **diagrama relacional** do sistema, representando as entidades e relacionamentos entre **alunos**, **livros** e **empréstimos**.

- [sql](sql): Nesse diretório estão os **scripts SQL** utilizados pelo sistema.
  * [01_Create_Tables_Biblioteca.sql](sql/01_Create_Tables_Biblioteca.sql): Script responsável pela criação das tabelas e definição das chaves primárias e estrangeiras.
  * [02_Insert_Core_Data.sql](sql/02_Insert_Core_Data.sql): Script responsável pela inserção de dados principais (como alunos e livros).
  * [03_Insert_Related_Data.sql](sql/03_Insert_Related_Data.sql): Script responsável pela inserção de dados relacionados (como registros de empréstimos).

- [src](src): Nesse diretório encontram-se os scripts do sistema:
  * [conexion](src/conexion): Nesse diretório encontra-se o **módulo de conexão com o banco de dados MySQL**. Esse módulo é responsável por abrir, fechar e gerenciar a comunicação com o servidor Aiven.
  * [controller](src/controller): Contém as **classes controladoras**, responsáveis por realizar inserção, alteração e exclusão de registros nas tabelas.
  * [model](src/model): Contém as **classes das entidades** (Aluno, Livro e Empréstimo) que representam o modelo lógico do banco de dados.
  * [reports](src/reports): Contém a classe responsável pela **geração de relatórios** do sistema.
  * [utils](src/utils): Contém scripts auxiliares, como o arquivo de **configuração do banco de dados** (`config.py`) e o **SplashScreen** exibido na inicialização.
  * [create_tables_and_records.py](src/create_tables_and_records.py): Script responsável por **criar as tabelas** e **inserir registros iniciais** no banco de dados. Deve ser executado antes do `principal.py` caso o banco ainda não possua as tabelas criadas.
  * [principal.py](src/principal.py): Script principal que apresenta o **menu interativo** do sistema, permitindo o cadastro, consulta e gerenciamento de alunos, livros e empréstimos.
  * [test.py](src/test.py): Script utilizado para **testar a conexão** com o banco de dados MySQL (Aiven).

---

## Execução Automática

Para simplificar o processo, o sistema possui o script [`run.py`], que executa **automaticamente** todas as etapas necessárias:

```shell
~$ python run.py
```

Esse comando irá:
1. Criar as tabelas no banco de dados (caso ainda não existam);
2. Inserir os registros iniciais;
3. Iniciar o sistema principal automaticamente.

---

## Instalação e Configuração

### 1️⃣ Criar e ativar o ambiente virtual (venv)
```shell
~$ python3 -m venv venv
~$ source venv/bin/activate
```

### 2️⃣ Atualizar ferramentas básicas do Python
```shell
~$ pip install --upgrade pip setuptools wheel
```

### 3️⃣ Instalar dependências do sistema
```shell
~$ sudo apt update
~$ sudo apt install -y build-essential python3-dev libatlas-base-dev libopenblas-dev libblas-dev gfortran
```

### 4️⃣ Instalar dependências do projeto
```shell
~$ pip install -r src/requirements.txt
```

---

## Estrutura do Banco de Dados

O banco de dados é composto por três entidades principais:

- **ALUNO:** Armazena os dados dos alunos (ID, nome, matrícula, turma, etc.);
- **LIVRO:** Armazena os dados dos livros disponíveis para empréstimo (ID, título, autor, editora, etc.);
- **EMPRÉSTIMO:** Relaciona os alunos aos livros emprestados, armazenando a data de retirada e devolução.

Todos os relacionamentos são controlados por **chaves estrangeiras**, garantindo a integridade referencial do sistema.

---

## Bibliotecas Utilizadas

As dependências estão listadas em:
- [requirements.txt](src/requirements.txt)

Para instalá-las:
```shell
~$ pip install -r src/requirements.txt
```

---

## Observações

- O arquivo [`src/utils/config.py`](src/utils/config.py) já está configurado para se conectar automaticamente ao banco de dados **MySQL Aiven**, não sendo necessária nenhuma modificação.
- O script [`run.py`](src/run.py) permite **executar todo o processo automaticamente**, desde a criação do banco até a inicialização do sistema.
- O sistema foi desenvolvido em **Python 3.10+** e testado em ambiente **Linux Ubuntu 22.04**.

---

**Demonstração no YouTube:**  
[Assista aqui](https://youtu.be/m6XD_HYXN8c)


## Desenvolvido por
- **Lucas Rufino**  
- **Lucas Pires**  
- **Jeronymo Moreira**

### Disciplina
**Banco de Dados – 2025/2**  
**Professor:** *Howard Roatti*
