#!/usr/local/bin/python
# coding: latin-1

arquivo = open('novo-arquivo.txt', 'w')
arquivo.close()

# Escrever em um arquivo
# Se o arquivo já existir ele irá sobrescrever todo o conteúdo.

arquivo = open('novo-arquivo.txt', 'w')
arquivo.write('nova linha')
arquivo.close()
