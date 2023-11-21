class Carro:
    # o que inicia a classe
    # atributos: marca, cor, combustível (primeiro atributo que se refere a propria classe: self)
    def __init__(self,marca,modelo,cor,combustivel):
        #criando os atributos
        self.marca = marca #variável
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        
        self.ligado = False
        self.velocidade = 0

    #criando métodos
    def ligar(self):
        if self.ligado:
            print("Carro já está ligado, nada acontece")
        else:
            print(f"{self.modelo}  Ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro Desligado")
            self.ligado = False
        else:
            print("Carro já está desligado, nada acontede")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade} km/h")
        else:
            print("Não é possível acelerar carro desligado")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade} km/h")
        else:
            print("Não é possível frear carro desligado")         
                
            
            

