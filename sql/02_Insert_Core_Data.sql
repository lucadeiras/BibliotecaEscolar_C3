USE biblioteca;

-- Inserindo livros
INSERT INTO livro (Genero, Titulo, Autor, Editora, Ano_Publicacao, Localizacao, Num_Paginas, Estoque, Disponivel) VALUES
    ('Suspense', 'Aurora nas Sombras', 'Fabien Vehlmann e Kerascoët', 'Darkside Books', 2019, 'Suspense, prateleira 8', 96, 4, TRUE),
    ('Aventura', 'O Incrível Hulk: Planeta Hulk', 'Greg Pak', 'Marvel Comics', 2006, 'Quadrinhos, prateleira 1', 428, 8, TRUE),
    ('Literatura Infantil', 'Alice no País das Maravilhas', 'Lewis Carroll', 'Darkside Books', 2019, 'Infantil, prateleira 12', 208, 10, TRUE),
    ('Didático', 'Por que o Café Esfria Tão Rápido?: e Outras Aplicações do Cálculo no seu dia', 'Oscar E. Fernandez', 'Blucher', 2016, 'Didáticos, prateleira 16', 200, 12, TRUE),
    ('Ficção Científica', 'A Máquina do Tempo', 'H. G. Wells', 'William Heinemann', 1895, 'Ficção Científica, prateleira 30', 84, 0, FALSE),
    ('Fantasia', 'Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 'Rocco', 2017, 'Fantasia, prateleira 1', 208, 7, TRUE);

-- Inserindo alunos
INSERT INTO aluno (Matricula, Nome, CPF, Email, Telefone, Endereco, Turma, Data_Nascimento) VALUES
    (24110359, 'Lucas Gonçalves Rufino de Souza', '11122233344', 'lucasdavi22@gmail.com', '21997962744', 'Rua Carlos Alves, 200', '4HC1A', '2004-06-12'),
    (11112222, 'Luciano Boa Figueredo Junior', '40028922777', 'lucianoboa38@gmail.com', '27996082362', 'Rua Monsenhor Raymundo Pereira Barros, 22', '2DB', '2005-05-09'),
    (22223333, 'Alexsander Amorim Borchardt', '55566677788', 'alexsanderamorim@hotmail.com', '27992525017', 'Rua Torta de Freitas, 666', '3HC1A', '2004-01-11'),
    (33445566, 'Davi Gonçalves Rufino de Souza', '12345678900', 'davigoku6@gmail.com', '27989867670', 'Rua Vasconcelos de Abreu, 45', '8MC1A', '2001-09-27');


