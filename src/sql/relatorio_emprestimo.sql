SELECT
    e.id_emprestimo,
    e.data_emprestimo,
    e.data_devolucao,
    a.matricula,
    a.nome AS nome_aluno,
    l.id_livro,
    l.titulo AS titulo_livro,
    l.autor AS autor_livro,
    CASE
        WHEN e.emprestado = TRUE THEN 'Em Curso'
        ELSE 'Devolvido'
    END AS status_emprestimo,
    CASE
        WHEN e.atraso = TRUE THEN 'Sim'
        ELSE 'Não'
    END AS houve_atraso,
    e.multa
FROM emprestimo e
INNER JOIN aluno a ON e.matricula = a.matricula
INNER JOIN livro l ON e.id_livro = l.id_livro
ORDER BY e.id_emprestimo DESC;

