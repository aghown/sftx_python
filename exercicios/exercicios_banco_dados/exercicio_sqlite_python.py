#1. Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

DB_PATH = BASE_DIR / "db" / "escola_v2.db"
print(DB_PATH)

conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

#2. Faça a query para pegar toda a tabela alunos e imprima na tela.
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()

print("=== Todos os alunos ===")
for aluno in alunos:
    print(aluno)

#3. Calcular média das notas e pegar top 10
cursor.execute("""
SELECT nome, (nota1 + nota2)/2 AS media
FROM Aluno
ORDER BY media DESC
LIMIT 10
""")

top10 = cursor.fetchall()

print("\n=== Top 10 alunos por média ===")
for aluno in top10:
    print(f"Aluno: {aluno[0]} | Média: {aluno[1]:.2f}")

#4. Fazer LEFT JOIN entre Aluno e Turma
cursor.execute("""
SELECT A.*, T.nome AS nome_turma
FROM Aluno AS A
LEFT JOIN Turma AS T
ON A.turma_id = T.id
""")

aluno_turma = cursor.fetchall()

print("\n=== Alunos com dados da turma ===")
for linha in aluno_turma:
    print(linha)


#5. Filtro para pegar apenas alunos da turma 2
cursor.execute("""
SELECT A.*, T.nome AS nome_turma
FROM Aluno AS A
LEFT JOIN Turma AS T
ON A.turma_id = T.id
WHERE A.turma_id = 2
""")

turma2 = cursor.fetchall()

print("\n=== Alunos da Turma 2 ===")
for linha in turma2:
    print(linha)

conexao.close()
