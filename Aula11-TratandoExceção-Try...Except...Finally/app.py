# Tratando exceções
# pode receber um tipo de dado que não está esperando
# conexão com banco de dados falhe
# tente ler arquivo sem abrir ele antes
# quando isso acontece aparece mensagem de erro e programa para
# o tratamento evita que mostre a mensagem gigante detalhando o erro

try:
    numero = int(input("Digite um número: "))
    print(numero)
except ZeroDivisionError:
    print("Divisão por zero não é possível")
except ValueError:
    print("Digite um valor válido.")
except:
    print("Erro inexperado")
finally: #independente do que ocorra, ele executa
    print("Sempre executa")

