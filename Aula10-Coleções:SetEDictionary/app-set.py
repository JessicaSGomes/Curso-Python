# Dados utilizados para armazenar coleções

# set é uma lista desordenada e não aceita valores duplicados (elementos únicos)
# set é mutável, mas seus valores individuais não são mutáveis
# set usa {} e não possui índices

frutas = {"maçã","Laranja","Abacaxi"}
print(frutas) # não imprime de forma ordenada

frutas.add("Pêra")
print(frutas)

# frutas.pop() irá remover um valor aleatório

# possibilidades
set1 = {"maçã","Laranja","Abacaxi"}
set1 = {0,3,56,-2}
set3 = {True, True, False, True} # irá imprimir sem repetir
set4 = {"Jessica",26,True}

print("-------------------------- OUTRAS INFOS")
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
#operações em conjuntos
uniao = conjunto_a.union(conjunto_b)
intersecao = conjunto_a.intersection(conjunto_b)
diferenca = conjunto_a.difference(conjunto_b)
print(uniao)
print(intersecao)
print(diferenca)

print("---------------------------")
lista_com_duplicatas = [1, 2, 3, 1, 2, 4]
conjunto_sem_duplicatas = set(lista_com_duplicatas)
#irá imprimir uma nova lista sem valores duplicados
