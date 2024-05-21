import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('bancoAPAM.db')
c = conn.cursor()

# Consulta para obter informações sobre as colunas da tabela
c.execute("PRAGMA table_info(bancoapam)")

# Obtendo os resultados da consulta
db = c.fetchall()
# Exibindo o nome das colunas
colunas = []
for coluna_db in db:
    colunas.append(coluna_db[1])

print(', '.join(colunas))

inter = ['?'] * len(colunas) # Lista de valores para serem inseridos na consulta

print(','.join(inter))
# Fechando a conexão com o banco de dados
conn.close()
