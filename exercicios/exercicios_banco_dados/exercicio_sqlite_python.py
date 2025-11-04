<<<<<<< HEAD
import sqlite3

# 1️⃣ Conectar ao banco de dados
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

# 2️⃣ Mostrar todos os alunos
print("=== TABELA DE ALUNOS ===")
cursor.execute("SELECT * FROM alunos;")
=======
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
cursor.execute("""
SELECT *
FROM Aluno
""")

alunos = cursor.fetchall()

print("=== Todos os alunos ===")
for aluno in alunos:
    print(aluno)

