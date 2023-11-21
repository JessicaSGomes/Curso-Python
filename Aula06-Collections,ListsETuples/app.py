#collections (coleção de dados) 
#Lists e Tuples: Estruturas de dados que servem para armazenar coleções de itens

#lists (listas de dados)
#lista pode ser add manualmente, um arquivo ou banco de dados
familia = ["Jessica", "Jean", "Luna", "Pedrito"] #entre chaves
#  indices     0         1       2        3
#  indices    -4        -3      -2       -1         

print(familia[0]) #retorna um índice
print(familia[-1]) #retorna um índice de trás pra frente
print(familia[1:]) #retorna a partir do índice 1
print(familia[1:3]) #exclui o último

familia[2] = "Luna Dog" #modifica o valor do indice
print(familia)

#funções que podem trabalhar com listas

#add mais valores à lista
familia.extend(["Mamaco", "Reginaldo"])
print(familia)

#add apenas um registro no final da lista
familia.append("Limbo")
print(familia)

#add um valor no meio da lista
familia.insert(3,"Mickey")
print(familia)

#remover um valor
familia.pop() #remove o último valor
familia.remove("Mickey")
print(familia)

#familia.clear() #apaga todos os itens da lista

print(familia.index("Jean")) #retorna o índice do item
print(familia.count("Jean")) #retorna a qtd de valores com mesmo nome

print(" ")
print("Ordenando")
idade_familia = [26, 27, 2, 1, 1, 1]
print(idade_familia)
idade_familia.sort() #ordenar os valores
print(idade_familia)
idade_familia.reverse() #após estar ordenada, pode inverter
print(idade_familia)

familia.sort() #ordena string em ordem alfabética
print(familia)
familia.reverse()
print(familia)


#como copiar uma lista
print(" ")
print("Copiando listas")

#cópia por referência
#aponta as duas variáveis para o mesmo objeto na memória do computador
familia2 = familia
print (f"familia2: {familia2}")
familia2.remove("Mamaco")
print(f"Familia2: {familia2}") 
print(f"familia: {familia}") #remove também da variavel de referencia

# .copy() faz uma 'cópia rasa'
#quando você deseja criar uma cópia do objeto original sem modificar o original
familia3 = familia2.copy() #a nova variável não referencia a anterior

#Tuples
#Diferença de Tuple e Listas: O Tuple é imutável e não pode ser alterado
print(" ")
print("Tuples")
coordenadas_lista = [-49,-36] #lista exemplo
coordenadas = (-49, -36) #tuple usa parênteses
# coordenadas.pop(), coordenadas[0] = -47 não funcionaria
#tuple não altera em nenhum momento no código
#funções que não alteram e não modificam o valor podem ser utilizadas
print(coordenadas)