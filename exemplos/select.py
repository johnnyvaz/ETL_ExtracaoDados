#!/usr/local/bin/python
# coding: latin-1
# Importamos a biblioteca:
import pymysql
conexao = pymysql.connect(db='carros', user='johnny', passwd='150907')
cursor = conexao.cursor()
cursor.execute("SELECT nome_dono FROM carros WHERE placa = 'ABC-1234'")
resultado = cursor.fetchall()
print('Dono do carro: ')

for linha in resultado :
    print(linha)
conexao.close()