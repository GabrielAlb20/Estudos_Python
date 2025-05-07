"""
Mapas -> Conhecidos em Python como Dicionários 

Dicionários em Python são representados por chaves {}

# Interar sobre Dicionários
for chave in receita:
    print(chave, receita[chave])

#ou 
for chave in receita:
    print(receita[chave])

# melhorando

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


    # acessando as chaves

print(receita)

print(receita.keys()) # Retorna as chaves do dicionário

for chave in receita.keys():
    print(receita[chave]) # Retorna os valores do dicionário


    
    # Acessando os valores do dicionário
print(receita.values()) # Retorna os valores do dicionário

for valor in receita.values(): # Modo Pythonico
    print(valor) # Retorna os valores do dicionário 

    
# Desempacotamento de dicionários

print(receita.items()) # Retorna uma lista de tuplas com as chaves e valores do dicionário
for chave, valor in receita.items():
    print(f'Em {chave} recebi R$ {valor}')



"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}




#Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * se os valores forem todos inteiros ou reais

print(sum(receita.values())) # Soma os valores do dicionário
print(max(receita.values())) # Retorna o valor máximo do dicionário
print(min(receita.values())) # Retorna o valor mínimo do dicionário	
print(len(receita)) # Retorna o tamanho do dicionário
print(receita) # Retorna o dicionário
