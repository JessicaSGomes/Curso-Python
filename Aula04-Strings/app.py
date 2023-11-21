#Strings: dentro de aspas

minha_string = "qualquer texto"
print(f"Concatenar {minha_string} em string")

#funções que pode usar com strings

print(minha_string.upper()) #deixar em maiúsculo
print(minha_string.lower()) #deixar tudo em minúsculo
print(minha_string.capitalize()) #deixar a primeira letra em maiúsculo

print(minha_string.isupper()) #maiusc retorna boolean false
print(minha_string.islower()) #minusc retorna boolean true
print(minha_string.strip()) #retira espações no início e/ou fim
print(minha_string.replace("qualquer", "meu")) #substitui uma palavra, texto ou letra
print(minha_string.replace("u", "U", 1)) # substitui apenas o primeiro u por U 
print(len(minha_string)) #tamanho da string
print(minha_string[2]) #retorna a letra na posição 2 - obs.: índice começa em 0
print(minha_string[2:5]) #retorna posição 2 à 5
print(minha_string[-4:-1]) #de trás pra frente
print(minha_string.index("l")) #retorna o índice

#verificar se o texto existe ou não 
x = "texto" in minha_string
print(x) #como existe texto na minha_string ele retorna true

#texto com multiplas linhas
outra_string = """linha 1,
Aqui tem texto em várias linhas,
linha 3.
""" #usando 3 aspas
print(outra_string)

outra_string2 = "linha 1,\nlinha 2,\nlinha 3." #caractere de escape \n
print(outra_string2)

outra_string3 = "adiciona \"aspas\" no texto"
print(outra_string3)
