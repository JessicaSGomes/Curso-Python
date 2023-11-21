num1 = 5
num2 = 3.5

#Qual o tipo da variável?
print(type(num1))
print(type(num2))

#converter um tipo de dado para outro
#passa para uma outra variável
a = float(num1)
print(a)
print(type(a))

b = int(num2)
print(b)
print(type(b))

#converter String para int e float
print("Converter String para int e float")
c = "5" #String
e = int(c) #int
print(e)
print(type(e))

#String decimal para inteiro: precisa passar a String para float e depois para inteiro
f = "5.3" #String
g = int(float(f)) #inteiro
print(f"f = {f} e g = {g}")