#Declarando variáveis
#String
nome = "Jessica"
#int
idade = 26
#float
altura = 1.52
#bool
is_female = True
#String
gosto_de = "Python"

#f-strings: possível formatar a string incorporando variáveis diretamente em strings

print("Hello World!")
print(f"Meu nome é {nome}.")
print(f"Estou estudando {gosto_de}.")
print(f"Eu tenho {idade} anos.")
print(f"{nome} estuda {gosto_de} e tem {idade} anos.")

#alterando o valor da variável

idade = 27
print(f"{nome} estuda {gosto_de} e tem {idade} anos.")