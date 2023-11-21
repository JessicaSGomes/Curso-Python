#input de usuário
nome = input("Digite seu nome: ")
idade = int(input(f"Qual a sua idade, {nome}? "))

nascimento = 2023 - idade

print(f"Seu nome é {nome}, sua idade é {idade} e você nasceu em {nascimento}")

#calculadora

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

resultado = num1 + num2

print(f"O resultado de {num1} + {num2} é {resultado}")
