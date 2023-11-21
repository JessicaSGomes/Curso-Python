# Dados utilizados para armazenar coleções

# Dictionary: existe uma chave e um valor
# dict: não são ordenados e não aceita valores duplicados
# dict: mutável

# criando dict meses que mapeia abreviações de meses para seus respectivos nomes completos
meses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Abr" : "Abril",
    "Mai" : "Maio",
    "Jun" : "Junho",
    "Jul" : "Julho",
    "Ago" : "Agosto",
    "Set" : "Setembro",
    "Out" : "Outubro",
    "Nov" : "Novembro",
    "Dez" : "Dezembro"
}

print(meses["Jun"]) # com [] se eu chamar um valor inválido irá dar erro
print(meses.get("abc")) # com o 'get' um valor inválido retorna um 'none'
print(meses.get("abc","Janeiro")) # segundo parâmetro é um valor padrão padrão que é retornado caso der algum erro

# qtd de itens na coleção
print(len(meses))
