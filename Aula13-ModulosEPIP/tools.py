# variaveis globais que armazenam valores numéricos
# por convenção, variáveis em maiúscula não podem ser alteradas (são constantes, apesar de que na prática pode alterar)
PI = 3.14
GRAVITY = 9.8

def get_extension(file):
    return file[file.index(".") +1:] 
# colchetes [] acessa os elementos de uma sequência
# index é usado para localizar a posição do ponto
# retorna o que vem depois do ponto (ou seja, a extensão do nome do arquivo)
# o ':' a seguir indica que queremos extrair uma fatia da string file


# definindo uma função que recebe uma lista de números como argumento
# com a função max() ele irá retornar o maior número
def highest_number(numbers):
    return max(numbers)