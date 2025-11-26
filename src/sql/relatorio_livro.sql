SELECT
    id_livro,
    genero,
    titulo,
    autor,
    editora,
    ano_publicacao,
    localizacao,
    num_paginas,
    estoque,
    CASE
        WHEN disponivel = TRUE THEN 'Sim'
        ELSE 'Não'
    END AS status_disponibilidade
FROM livro
ORDER BY titulo, autor;
