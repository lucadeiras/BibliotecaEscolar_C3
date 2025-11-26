USE biblioteca;

-- ===========================================
-- Inserção de Empréstimos de Exemplo
-- ===========================================
-- Observação:
-- - Garante que o SELECT de ID_Livro retorne no máximo 1 linha
-- - Usa LIMIT 1 em todos os subselects
-- - Evita erros de "Subquery returns more than 1 row"
-- ===========================================

-- Prazo de devolução padrão: 7 dias
-- Multa: R$ 2,50 por dia de atraso

INSERT INTO emprestimo 
    (matricula, id_livro, data_emprestimo, data_devolucao, atraso, multa, emprestado)
VALUES 
(
    24110359, 
    (SELECT id_livro FROM livro WHERE titulo = 'Aurora nas Sombras' LIMIT 1),
    '2025-10-15',
    '2025-10-23',
    FALSE,
    0.00,
    TRUE
),
(
    22223333, 
    (SELECT id_livro FROM livro WHERE titulo = 'O Incrível Hulk: Planeta Hulk' LIMIT 1),
    '2025-09-12',
    '2025-10-14',
    TRUE,
    37.50,
    FALSE
),
(
    33445566, 
    (SELECT id_livro FROM livro WHERE titulo = 'Harry Potter e a Pedra Filosofal' LIMIT 1),
    CURDATE(),
    DATE_ADD(CURDATE(), INTERVAL 7 DAY),
    FALSE,
    0.00,
    TRUE
),
(
    24110359, 
    (SELECT id_livro FROM livro WHERE titulo = 'Alice no País das Maravilhas' LIMIT 1),
    '2025-10-06',
    '2025-10-16',
    TRUE,
    5.00,
    FALSE
),
(
    11112222, 
    (SELECT id_livro FROM livro WHERE titulo = 'Aurora nas Sombras' LIMIT 1),
    '2025-09-02',
    '2025-09-11',
    FALSE,
    0.00,
    FALSE
),
(
    24110359, 
    (SELECT id_livro FROM livro WHERE titulo = 'Por que o Café Esfria Tão Rápido?: e Outras Aplicações do Cálculo no seu dia' LIMIT 1),
    '2025-06-30',
    '2025-07-15',
    TRUE,
    10.00,
    FALSE
),
(
    22223333, 
    (SELECT id_livro FROM livro WHERE titulo = 'Harry Potter e a Pedra Filosofal' LIMIT 1),
    CURDATE(),
    DATE_ADD(CURDATE(), INTERVAL 7 DAY),
    FALSE,
    0.00,
    TRUE
);

-- ===========================================
-- 🔚 Fim do arquivo
-- ===========================================
