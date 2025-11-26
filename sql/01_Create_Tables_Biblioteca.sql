-- ==========================================
--  SCRIPT: 01_Create_Tables_Biblioteca.sql
--  OBJETIVO: Criar o banco de dados e tabelas do sistema da Biblioteca Escolar
--  CRIADO POR: 
--      • Lucas Rufino
--      • Lucas Pires
--      • Jeronymo Moreira
--  VERSÃO: Final
-- ==========================================

-- 🔄 Remove o banco de dados anterior para garantir ambiente limpo
DROP DATABASE IF EXISTS biblioteca;

-- 🏗️ Cria novamente o banco e o seleciona
CREATE DATABASE biblioteca;
USE biblioteca;

-- ==============================
-- 🧱 TABELA: LIVRO
-- ==============================
CREATE TABLE livro (
    id_livro INT AUTO_INCREMENT NOT NULL,
    genero VARCHAR(50) NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    editora VARCHAR(100) NOT NULL,
    ano_publicacao INT NOT NULL,
    localizacao VARCHAR(100) NOT NULL,
    num_paginas INT NOT NULL,
    estoque INT NOT NULL,
    disponivel BOOLEAN NOT NULL,
    CONSTRAINT livro_pk PRIMARY KEY (id_livro)
);

-- ==============================
-- 🧱 TABELA: ALUNO
-- ==============================
CREATE TABLE aluno (
    matricula INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    turma VARCHAR(5) NOT NULL,
    data_nascimento DATE NOT NULL,
    CONSTRAINT aluno_pk PRIMARY KEY (matricula)
);

-- ==============================
-- 🧱 TABELA: EMPRESTIMO
-- ==============================
CREATE TABLE emprestimo (
    id_emprestimo INT AUTO_INCREMENT NOT NULL,
    matricula INT NOT NULL,
    id_livro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    atraso BOOLEAN NOT NULL DEFAULT 0,
    multa DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    emprestado BOOLEAN NOT NULL DEFAULT 1,
    CONSTRAINT emprestimo_pk PRIMARY KEY (id_emprestimo),
    CONSTRAINT livro_emprestimo_fk FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT aluno_emprestimo_fk FOREIGN KEY (matricula) REFERENCES aluno (matricula)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ==============================
-- ✅ FIM DO SCRIPT
-- ==============================
