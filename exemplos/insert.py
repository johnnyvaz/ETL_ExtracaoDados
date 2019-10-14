#!/usr/local/bin/python
# coding: latin-1

# Importamos a biblioteca:
import pymysql

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='carros', user='johnny', passwd='150907')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("INSERT INTO carros (placa, nome_dono) VALUES ('ABC-1234', 'Joao')")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()