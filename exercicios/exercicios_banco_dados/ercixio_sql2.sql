.tables

.schema Aluno

-- 1.
SELECT COUNT(*) AS total_alunos
FROM Aluno;

-- 2.
SELECT MIN(mensalidade) AS menor_mensalidade
FROM Curso;

-- 3.
SELECT MAX(nota1) AS maior_nota1
FROM Aluno;

-- 4.
SELECT SUM(mensalidade) AS total_mensalidades
FROM Curso;

-- 5.
SELECT AVG(nota2) AS media_nota2
FROM Aluno;
