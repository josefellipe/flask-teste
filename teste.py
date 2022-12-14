import sqlite3

conexao = sqlite3.connect("testes-aws.db")

comando = "INSERT INTO retorno(mensagem) VALUES ('Isto é um teste')"

cursor = conexao.cursor()
cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()