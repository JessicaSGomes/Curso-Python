# criando uma matriz: listas de listas
matriz_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matriz_numeros:
    print(linha)
    for coluna in linha: # loop 'for' aninhado: variável coluna percorre cada elemento dentro da linha da matriz
        print(coluna)

# Então, para cada linha na matriz, estamos indo além e examinando cada elemento individualmente, 
# e a variável coluna representa cada um desses elementos durante a iteração