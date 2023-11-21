# Manipulando arquivos

# open("caminho","r")

# r - leitura
# a - Append / incrementar
# w - Escrita
# x - Criar arquivo novo
# r+ - Leitura + Escrita

# arquivo = open("Aula12-ManipulandoArquivos/test3.txt","x")
# usa "a" adiciona no arquivo que existe
# usa 'w' limpa o arquivo e começa um novo

# print(arquivo.readable()) # esse arquivo pode ser lido?
# print(arquivo.read()) # conteúdo do arquivo é impresso no console

# print(arquivo.readline()) #retorna a primeira linha
# print(arquivo.readline()) # vai lendo linha por linha
# print(arquivo.readline())

# lista = arquivo.readlines() #transforma em uma 'lista'
# print(lista)
# print(lista[3])

# arquivo.write("C\n") #adicionando conteúdo
# arquivo.write("C++\n")

# arquivo.close() # fecha o arquivo após a 'leitura'


# EXCLUSÃO DE ARQUIVO: precisa importar, pois não é uma função própria
import os
if os.path.exists("Aula12-ManipulandoArquivos/test2.txt"):
    os.remove("Aula12-ManipulandoArquivos/test2.txt") #remove este arquivo - precisa estar fechado para remover
else:
    print("Arquivo não existe")

# Removendo pasta: ela antes deve estar vazia
# os.rmdir("Aula12-ManipulandoArquivos/novapasta")