"""
Sorted 

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sorte()
só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados


# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Ordena do menor para o maior

print(numeros)


numeros = [6, 1, 8, 2]
print(numeros)
print(set(sorted(numeros)))

# Adicionando parâmetros ao sorted()

print(sorted(numeros))
print(sorted(numeros, reverse = True))



# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu amo Python', 'Eu amo Django']},
    {'username': 'Lucas', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': [], "cor": "Amarelo"},
    {'username': 'Alvaro', 'tweets': []},
    {'username': 'Nayara', 'tweets': ['Eu gosto do meu gato', 'Vou sair hoje']},
    {'username': 'Gall', 'tweets': [],  "cor": "Preto", "musica": 'rock'},
]

print(usuarios)

# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key =lambda usuario: usuario['username'], reverse=True))

# Ordenando pelo números de tweets
print(sorted(usuarios, key =lambda usuario: len(usuario)["tweets"]))


"""

# Último exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': "Too old to rock'in'roll, too ynoung to die", "tocou": 32},
]

# Ordena da menos tocada, para a mais tocada.
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada, para a menos tocada.
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
