#!/usr/local/bin/python
# coding: latin-1

# Inserir conteúdo ao já existente (adicionar)

arquivo = open('novo-arquivo.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append('Nova linha')   # insira seu conteúdo

arquivo = open('novo-arquivo.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()