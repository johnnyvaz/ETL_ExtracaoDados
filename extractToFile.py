#!/usr/local/bin/python
# coding: latin-1
# Importamos a biblioteca:
import pymysql
conexao = pymysql.connect(db='carros', user='johnny', passwd='150907')
cursor = conexao.cursor()
cursor.execute("SELECT nome_dono FROM carros WHERE placa = 'ABC-1234'")
resultado = cursor.fetchall()

arquivo = open('carros.txt', 'w')
for linha in resultado :
    arquivo.write(str(linha))

arquivo.close()
conexao.close()

