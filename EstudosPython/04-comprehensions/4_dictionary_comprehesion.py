"""
Dicionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4, 5]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4, 5) # 1, 2, 3, 4, 5 são os elementos da tupla

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4,}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} # chave: valor


# Sintaxy

{chave: valor for chave, valor in interável}


# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


numeros = [1, 2, 3, 4, 5]

dicionario = {numero: numero ** 2 for numero in numeros}

print(dicionario) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



"""

# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res) # {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}