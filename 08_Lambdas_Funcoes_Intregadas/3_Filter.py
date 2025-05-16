"""
Filter 

filter() -> Serve para filtrar dados de uma determinada coleção


# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)  # 1.8833333333333333

print(f' Média: {media}')
# Definindo uma função que verifica se o valor é maior que a média

# OBS: Assim como a função map(), a função filter() recebe dois parâmetros: O primeiro é a função que queremos aplicar e o segundo é o iterável. Retorna um Filter Object.
res = filter(lambda x: x > media, dados)
print(type(res))  # <class 'filter'>
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', 'Equador', '', '', 'Venezuela',]

res = filter(None, paises)
print(type(res))  # <class 'filter'>

print(list(res))  # ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', 'Equador', '', '', 'Venezuela']
# OBS: Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.



paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', 'Equador', '', '', 'Venezuela',]

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)  # None é o mesmo que lambda x: x > 0
res = filter(lambda pais: pais != '', paises)  # None é o mesmo que lambda x: x > 0


print(list(res))  



# A diferenca entre map() e filter() é:

# map() -> Recebe dois parametros, uma função e um interável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parametros, uma função e um interável e retorna um objeto filtrando os elementos do iterável que atendem a condição da função.




# Exemplo mais complexo

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu amo Python', 'Eu amo Django']},
    {'username': 'Lucas', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Alvaro', 'tweets': []},
    {'username': 'Nayara', 'tweets': ['Eu gosto do meu gato', 'Vou sair hoje']},
    {'username': 'Gall', 'tweets': []},
]


#print(usuarios)

# Filtrando os usuários que não possuem tweets

# Forma comum
#inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
#print(f'Usuários inativos: {inativos}')

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""

# Como combinar filter() e map() para filtrar e transformar dados

nomes = ['Samuel', 'Alvaro', 'Nayara',]

# Devemos criar uma lista contendo 'Sua instrutora é + nome, desde que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)  # ['Sua instrutora é Alvaro', 'Sua instrutora é Nayara']
# OBS: Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.