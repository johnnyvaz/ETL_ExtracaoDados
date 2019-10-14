#!/usr/local/bin/python
# coding: latin-1
# Importamos a biblioteca:
import pymysql
conexao = pymysql.connect(db='carros', user='johnny', passwd='150907')
cursor = conexao.cursor()
cursor.execute("UPDATE carros SET nome_dono = 'Joaquim' WHERE placa = 'ABC-1234'")
conexao.commit()
conexao.close()