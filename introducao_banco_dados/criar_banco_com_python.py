import sqlite3
from pathlib import Path

db_connection = sqlite3.connect("introducao_banco_dados/db/loja2.db")

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM clientes")
for linha in cursor:
    print(linha)

cursor.execute("""CREATE TABLE clientes (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nome VARHAR(255) NOT NULL,
               endereco VARCHAR(255) NOT NULL,
               telefone INT(11) NOT NULL
               )""")

sql = "INSERT INTO clientes * VALUES (?, ?, ?)"
val = [("Fred", "Aquela rua", 81955555555), ("maria", "Rua 2", 12345678901)]
cursor.executemany(sql, val)

db_connection.commit()

cursor.execute("SELECT * FROM clientes")

resultado = cursor.fetchall()

for linha in resultado:
    print(resultado)
