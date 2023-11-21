#declara a função com def e atributos fica dentro dos parênteses
def big_mac():
    print("Sanduiche big mac") #o que está dentro da função: TAB
#Chamando a função
#big_mac()

# nome será uma variável
# função recebe 'nome' e imprime uma mensagem
def fazer_big_mac(nome):
    print(f"Sanduiche big mac do(a) {nome}")

# chamando a função
# fazer_big_mac("Jessica")
# fazer_big_mac("Jean")
# fazer_big_mac("Luna")

# função recebe argumento 'tamanho' e imprime uma mensagem 
def fazer_batata(tamanho):
    print(f"Batata {tamanho}")

# função recebe dois argumentos 'tipo' e 'tamanho' e imprime mensagem
def preparar_refrigerante(tipo_refri,tamanho_refri):
    print(f"{tipo_refri} {tamanho_refri}")

# fazer_big_mac("Jessica")
# fazer_batata("Pequena")
# preparar_refrigerante("Coca","Média")

# função que chama as funções anteriores com argumentos específicos
def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

fazer_combo_big_mac("Jessica","P","Coca","M")

#função para somar números
# return: sair de uma função e retornar um valor
def soma_numeros(num1,num2):
    return num1 + num2

# resultado = soma_numeros(15,20)
# print(resultado)

#qual o maior número?
def maior_numero(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_numero = lista_num[0]
    return maior_numero

resultado = maior_numero([234,45,22,32,-45,-30, 1090, 309, 333, 540])
print(" ")
print(resultado)