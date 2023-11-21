# i = 1

# while i < 10:
#     print(i)
#     i += 1

crianças = ["Ana", "Lucas", "Bruno"]
#item é uma variável
# for item in crianças:
#     print(item)

# canal = "Refatorando"
# 'for' baseado no tamanho do meu índice
# for letra in canal:
#     print(letra)

# 'for' baseado em um range(recebe 3 atributos 1°=start, 2°=stop(único obrigatório), 3°=step)
# for index in range(2, 20, 2):
#     print(index)


# utilizando o loop para percorrer uma lista chamada criança
# imprime cada elemento da lista juntamente com o índice
# for index in range(len(crianças)): #cria loop 'for'. O range(len(crianças)) gera uma sequência de num de 0 a len(crianças) - 1 
#     print(crianças[index], index) #imprime o nome da criança em determinado índice e o índice

# print(len(crianças)) # igual a 3


for index in range(5): # índice começa do zero
    if index == 0:
        print("primeira linha")
    else:
        print(f"outras linhas {index}")




    