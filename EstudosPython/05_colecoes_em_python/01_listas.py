'''type([])

essa sessão é muito importante, 
listas(lists) ciencia de dados big date, IA (BIO/DNA)

lista4 = list((range(11))) # cria uma lista com os números de 0 a 10
print(lista4)
# Criando uma lista de números inteiros

lista1 = [6, 2, 8, 4, 38, 5, 1, 3, 7]
print(lista1)  # Exibe [1, 2, 3, 4, 5]

# Criando uma lista de strings
lista2 = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
print(lista2)  # Exibe ['G', 'F', 'E', 'D', 'C', 'B', 'A']

# Criando uma lista vazia
lista3 = []
print(lista3)  # Exibe [] (lista vazia)

# Criando uma lista com números de 0 a 10
lista4 = list(range(11))
print(lista4)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista5 = list('Python')  # Converte a string 'Python' em uma lista de caracteres
print(lista5)  # Exibe ['P', 'y', 't', 'h', 'o', 'n']

# Podemos facilmente checar se detrminado elemento está na lista

if 8 in lista4:
    print('8 está na lista4')
else:
    print('8 não está na lista4')



# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
# Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38]

# ordena uma lista de str 
lista5.sort()
print(lista5) # Exibe ['P', 'h', 'n', 'o', 't', 'y']

# podemos facilmente contr o número de ocorrencias de um valor em uma lista
print(lista1.count(8))  # Exibe 1 (o número 8 aparece uma vez na lista1)
print(lista5.count('e')) # Exibe 0 (a letra 'e' não está na lista5)

# adicionar elementos a lista
print(lista1)

para adicionar elementos na lista, podemos usar os métodos append().

lista1.append(42)  # Adiciona o número 42 ao final da lista1
print(lista1)

#OBS: com append, nós só conseguimos adicionar 1 elemento por vez
#se quisermos adicionar mais de um elemento, podemos usar o método extend().

lista1.append([1, 2, 3])  # Adiciona a lista [1, 2, 3] ao final da lista1
print(lista1)  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3]]

if [1, 2, 3] in lista1:
    print('A lista [1, 2, 3] está na lista1')
else:
    print('A lista [1, 2, 3] não está na lista1')


lista1.extend([1, 2, 3])  # Adiciona os elementos da lista [1, 2, 3] ao final da lista1 VALOR ADICIONAL
print(lista1)  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3]

podemos inserir um novo elemento na lista informando a posição do índice
OBS: isso não substitui o elemento que já está na posição, apenas adiciona um novo elemento na posição informada
Exemplo: Adicionando o número 0 na posição 0 da lista1
lista1.insert(0, 0)  # Adiciona o número 0 na posição 0 da lista1
print(lista1)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3]

# podemos facilmente juntar duas listas
# Exemplo: Juntando a lista1 e a lista2
lista6 = lista1 + lista2  # Junta a lista1 e a lista2
print(lista6)  # Exibe [0, 1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3, 'G', 'F', 'E', 'D', 'C', 'B', 'A']

# podemos facilmente inverter uma lista
lista.reverse() inverte a lista original
lista1.reverse()  # Inverte a lista1
lista2.reverse()  # Inverte a lista2
print(lista1)  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1]   

forma 2
print(lista1[::-1])  # Exibe [1, 2, 3, 4, 5, 6, 7, 8, 38, [1, 2, 3], 1, 2, 3] (inverte a lista1 sem alterar a original)
print(lista2[::-1])  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1] (inverte a lista1 sem alterar a original)
print(lista1)  # Exibe [3, 2, 1, [1, 2, 3], 38, 8, 7, 6, 5, 4, 3, 2, 1] (inverte a lista1 sem alterar a original)

copiar uma lista 
lista10 = lista2.copy() # Copia a lista2 para a lista10
print(lista10)  # Exibe ['A', 'B', 'C', 'D', 'E', 'F', 'G'] (copia a lista2 para a lista10)

Podemos remover facilmente o último elemento de uma lista
OBS: o Pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()  # Remove o último elemento da lista5
print(lista5) # Exibe ['G', 'a', 'b', 'r', 'i', 'e']

Podemos remover um elemento pelo índice
OBS: Os elementos á direita deste índice são deslocados para a esquerda
OBS: Se não houver elemento no índice informado, teremos o erro IndexError
listaa5.pop(2)  # Remove o elemento na posição 2 da lista5
print(lista5) # Exibe ['G', 'a', 'r', 'i', 'e']

podemos facilmente remover todos os elementos (zerar lista)
print(lista5)  # Exibe ['G', 'a', 'b', 'r', 'i', 'e', 'l']
lista5.clear()  # Remove todos os elementos da lista5
print(lista5)  # Exibe [] (lista vazia)

Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3  # Repete a lista nova 3 vezes
print(nova)  # Exibe [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3  # Repete a lista nova 3 vezes
print(nova)  # Exibe [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Podemos facilmente converter uma string para uma lista
#Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()  # Converte a string em uma lista de palavras
print(curso)

# Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # Converte a string em uma lista de palavras, separando por vírgula
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)  # Exibe 'Programação em Python Essencial'

curso = 'Programação$em$Python:$Essencial'
curso = ''.join(curso.split('$'))
print(curso)  # Exibe 'ProgramaçãoemPython:Essencial'

# Abaixo estamos falando: pega a lista6, coloca $ entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)  # Exibe 'Programação$em$Python$Essencial'

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando tipos
Lista6 = [1, 2.34, True, 'Gabriel', 'm', [1, 2, 3], 81992580275]
print(Lista6)
print(type(Lista6))  # Exibe <class 'list'> (o tipo da variável Lista6 é uma lista)

# Iterando sobre listas

# Exemplo 1 - Utilizando for 
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
    print(soma)


# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto ao carrinho ou digite "sair" para finalizar: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#Utiliando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)  # Exibe [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)  # Exibe [1, 2, 3, 4, 5]         

# Fazemos acesso aos elementos de forma indexada
#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco',]
print(cores[0])  # Exibe 'verde'
print(cores[1])  # Exibe 'amarelo'
print(cores[2])  # Exibe 'azul'
print(cores[3])  # Exibe 'branco'

# Fazer acesso aos elementos de forma indexada negativa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao início do próximo elemento.
#           0         1        2         3
#          -4        -3       -2        -1
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])  # Exibe 'branco' (último elemento da lista)
print(cores[-2])  # Exibe 'azul' (penúltimo elemento da lista)
print(cores[-3])  # Exibe 'amarelo' (antepenúltimo elemento da lista)
print(cores[-4])  # Exibe 'verde' (último elemento da lista)
#print(cores[-5]) #ERRO: IndexError: pois não existe o índice -5 na lista cores


cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)  # Exibe cada cor da lista cores

indice = 0
while indice < len(cores):
    print(cores[indice])  # Exibe cada cor da lista cores
    indice = indice + 1


cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)  # Exibe o índice e a cor correspondente na lista cores

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista) # Exibe [42, 42, 33, 33, 42]


# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista
# ÍNDICE:  0  1  2  3  4  5
numeros = [5, 6, 7, 8, 5, 9, 10]

# Em qual índice da lista está o valor 6
print(numeros.index(6)) # Exibe 1 (o número 9 está no índice 1 da lista numeros)

# Em qual índice da lista está o valor 9
print(numeros.index(9)) # Exibe 4 (o número 10 está no índice 4 da lista numeros)

# OBS: Caso não tenha esta elemento na lista, será apresentado erro ValueError
# print(numeros.index(11)) # ValueError: 11 is not in list
print(numeros.index(5)) # Retorna o índice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do índice 1
print(numeros.index(5, 2)) # Buscando a partir do índice 2
print(numeros.index(5, 3)) # Buscando a partir do índice 3
print(numeros.index(5, 4)) # Buscando a partir do índice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# print(numeros.index(11, 1)) # ValueError: 11 is not in list

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(8, 3, 6)) # Buscando a partir do índice 3 até o índice 6
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError


#  Revisão de slicing 

# lista[inicio:fim:passo]
# range(inicio, fim, passo)

# Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes da lista
print(lista[::]) # Pega todos os elementos da lista 

# Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2]) # começa em 0, pega até o índice 2 - 1

print(lista[:4]) # começa em 0, pega até o índice 4 - 1

print(list[1:3]) # começa em 1, pega até o índice 3 - 1


# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) # começa em 1, pega até o índice 2 - 1, e pula de 2 em 2
print(lista[::2]) # começa em 0, pega até o índice 2 - 1, e pula de 2 em 2

# invertendo valores em uma lista

nomes = ['Gabriel', 'Gomes']

#EXEMPLO 1:
# Fazendo a troca de valores em uma lista com o operador de atribuição
nomes[0], nomes[1] = nomes[1], nomes[0] # Troca os valores de nomes[0] e nomes[1]
print(nomes)

# EXEMPLO 2:
# Fazendo a troca de valores em uma lista com o método reverse()
nomes = ['Gabriel', 'Gomes']
nomes.reverse() # Inverte a lista nomes
print(nomes) # Exibe ['Gomes', 'Gabriel']

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# Se os valres forem todos inteiros ou reais 

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Exibe 21 (soma todos os elementos da lista)
print(max(lista)) # Exibe 6 (valor máximo da lista)
print(min(lista)) # Exibe 1 (valor mínimo da lista)
print(len(lista)) # Exibe 6 (tamanho da lista)


# Transformar uma lista em tupla

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1)
print(type(lista1))

tupla  = tuple(lista1) # Transforma a lista em uma tupla
print(tupla)
print(type(tupla)) # Exibe <class 'tuple'> (o tipo da variável tupla é uma tupla)

                                                                
  # Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista # Desempacota a lista em 3 variáveis

print(num1)  # Exibe 1 (primeiro elemento da lista)
print(num2)  # Exibe 2 (segundo elemento da lista) 
print(num3)  # Exibe 3 (terceiro elemento da lista)

# OBS: Se tivermos mais elementos para desepacotar do que variáveis, teremos o erro ValueError                                                               
                                                                  
                                                                   






                                                                     
                                                                      
                                                                        '''
'''type([])

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['G', 'A', 'B', 'R', 'I', 'E', 'L']
lista3 = []
lista4 = list(range(11))
lista5 = list('Gabriel')'''


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 

lista = [1, 2, 3]
print(lista)

nova = lista.copy() # Copia a lista para a nova lista
print(nova) # Exibe [1, 2, 3]

nova.append(4) # Adiciona o número 4 na nova lista

print(lista)
print(nova) # Exibe [1, 2, 3, 4] (a lista original não foi alterada)

# Veja que ao utilizarmos o método copy(), a nova lista é uma cópia da lista original, mas não é uma referência à lista original.
# Ou seja, se alterarmos a nova lista, a lista original não será alterada.
# É chamado de Deep Copy (Cópia profunda)

# Forma 2 - Shallow Copy (Cópia rasa)

lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova) # Exibe [1, 2, 3, 4] (a lista original foi alterada)

# Veja que ao utilizarmos a atribuição, a nova lista é uma referência à lista original.
# Ou seja, se alterarmos a nova lista, a lista original também será alterada.