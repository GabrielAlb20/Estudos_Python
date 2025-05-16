"""
Módulo Collections - Counter (Contador)

Collections -> High - Perfomance Container Datetypes

Counter -> Recebe um interável como parametro e cria um objeto do tipo Collections Counter que é parecido 
com um dicionário, contendo como chave o elemento da lista passada como parametro e com valor a quantidade
de ocorrencias desse elementos


# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer interável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 4, 3: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave  e colocou como valor a quantidade de ocorrencias.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


"""

from collections import Counter

# Exemplo 3

texto = """ Singin' and Swingin' and Gettin' Merry Like Christmas é o terceiro livro da série autobiográfica de sete volumes da escritora
 norte-americana Maya Angelou. Baseado nos anos entre 1949 e 1955, o livro abrange o início da fase adulta de Angelou. Neste volume,
 ela descreve suas lutas para apoiar seu filho, formar relacionamentos significativos e estabelecer uma carreira de sucesso no mundo 
 do entretenimento. A publicação da obra em 1976 foi a primeira vez que uma mulher afro-americana expandiu sua história de vida para um terceiro
 volume. A acadêmica Dolly McPherson intitula o livro como "um retrato gráfico do eu adulto em flor", enquanto o crítico Lyman B. Hagen o chama
 de "uma jornada de descoberta e renascimento" """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

#print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(10))

