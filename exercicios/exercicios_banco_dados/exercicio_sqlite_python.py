import sqlite3

# 1️⃣ Conectar ao banco de dados
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

# 2️⃣ Mostrar todos os alunos
print("=== TABELA DE ALUNOS ===")
cursor.execute("SELECT * FROM alunos;")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

# 3️⃣ Calcular média entre nota1 e nota2, ordenar e pegar os 10 maiores
print("\n=== TOP 10 ALUNOS POR MÉDIA ===")
cursor.execute("""
    SELECT nome, (nota1 + nota2)/2 AS media
    FROM alunos
    ORDER BY media DESC
    LIMIT 10;
""")
top10 = cursor.fetchall()
for aluno in top10:
    print(aluno)

# 4️⃣ Fazer LEFT JOIN entre Aluno e Turma e mostrar todos os dados
print("\n=== LEFT JOIN ALUNO + TURMA ===")
cursor.execute("""
    SELECT alunos.*, turmas.*
    FROM alunos
    LEFT JOIN turmas
    ON alunos.turma_id = turmas.id;
""")
dados_join = cursor.fetchall()
for linha in dados_join:
    print(linha)

# 5️⃣ Filtrar apenas os alunos da turma 2
print("\n=== ALUNOS DA TURMA 2 ===")
cursor.execute("""
    SELECT alunos.*, turmas.*
    FROM alunos
    LEFT JOIN turmas
    ON alunos.turma_id = turmas.id
    WHERE turmas.id = 2;
""")
turma2 = cursor.fetchall()
for linha in turma2:
    print(linha)

# Encerrar conexão
conexao.close()
